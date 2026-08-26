import frappe
from frappe.utils import nowdate

@frappe.whitelist(allow_guest=True)
def get_store_profile(slug):
    stores = frappe.get_all(
        "Business",
        filters={"slug": slug},
        fields=["name", "business_name", "description", "image", "banner", "is_active"],
        limit=1
    )

    if not stores:
        return None

    store = stores[0]

    child_banners = frappe.get_all(
        "Banner Link",
        filters={
            "parent": store.name,
            "parentfield": "section_banner"
        },
        fields=["banner"],
        order_by="idx asc"
    )

    section_banner_data = []

    for row in child_banners:
        if row.banner:
            banner_detail = frappe.db.get_value(
                "Banner",
                row.banner,
                ["title", "banner"],
                as_dict=True
            )

            if banner_detail:
                section_banner_data.append({
                    "banner_id": row.banner,
                    "title": banner_detail.title,
                    "image": banner_detail.banner
                })

    store["section_banner"] = section_banner_data

    return store


@frappe.whitelist(allow_guest=True)
def get_items(slug, recomended=None, item_group=None, exclude_special=None):
    business = frappe.get_all(
        "Business",
        filters={"slug": slug},
        fields=["name"],
        limit=1
    )

    if not business:
        return []

    business_name = business[0]["name"]

    filters = {
        "business": business_name
    }

    if recomended:
        filters["recomended"] = 1

    if item_group:
        filters["item_group"] = item_group

    items = frappe.get_all(
        "Item",
        filters=filters,
        fields=[
            "name",
            "item_name",
            "item_group",
            "image",
            "description",
            "business",
            "recomended",
            "slug",
            "cod",
            "delivery",
        ],
    )

    if not items:
        return []

    item_docnames = [i["name"] for i in items]

    prices = frappe.get_all(
        "Price",
        filters={"item_name": ["in", item_docnames]},
        fields=["item_name", "price"],
    )

    price_map = {
        p["item_name"]: p["price"]
        for p in prices
    }

    # --- HITUNG DISKON AKTIF UNTUK SEMUA ITEM (bukan cuma di get_discounted_items) ---
    today = nowdate()
    active_discounts = frappe.get_all(
        "Discount",
        filters={
            "business": business_name,
            "start_date": ["<=", today],
            "end_date": [">=", today],
        },
        fields=["name", "amount"],
    )

    discount_map = {}
    if active_discounts:
        discount_names = [d["name"] for d in active_discounts]
        discount_items = frappe.get_all(
            "Item Discount",
            filters={
                "parent": ["in", discount_names],
                "item": ["in", item_docnames],
            },
            fields=["item", "parent"],
        )
        parent_amount_map = {d["name"]: d for d in active_discounts}
        for row in discount_items:
            if row.item:
                discount_map[row.item] = parent_amount_map.get(row.parent)
    # ------------------------------------------------------------------------------

    group_ids = list(set([i["item_group"] for i in items if i.get("item_group")]))
    group_map = {}
    if group_ids:
        groups = frappe.get_all(
            "Item Group",
            filters={"name": ["in", group_ids]},
            fields=["name", "item_group_name", "slug"],
        )
        group_map = {g["name"]: g for g in groups}

    result = []

    for item in items:
        base_price = price_map.get(item["name"]) or 0
        item["price"] = base_price

        group = group_map.get(item.get("item_group"))
        item["item_group_name"] = group["item_group_name"] if group else None
        item["item_group_slug"] = group["slug"] if group and group.get("slug") else None

        discount_info = discount_map.get(item["name"])
        if discount_info and base_price:
            discount_amount = float(discount_info["amount"] or 0)
            item["discount_percent"] = discount_amount
            item["discounted_price"] = round(base_price - (base_price * discount_amount / 100))
        else:
            item["discount_percent"] = 0
            item["discounted_price"] = base_price

        # Kalau dipanggil dari "Semua Produk", skip item yang recomended atau lagi diskon
        if exclude_special:
            is_recomended = item.get("recomended") == 1
            is_discounted = item["discount_percent"] > 0
            if is_recomended or is_discounted:
                continue

        result.append(item)

    return result

@frappe.whitelist(allow_guest=True)
def get_item_groups_by_store(slug):
    business_id = frappe.db.get_value("Business", {"slug": slug}, "name")

    if not business_id:
        return []

    business_items = frappe.get_all(
        "Item",
        filters={"business": business_id},
        fields=["item_group"]
    )

    active_item_groups = list(set([item.item_group for item in business_items if item.item_group]))

    if not active_item_groups:
        return []

    item_group_details = frappe.get_all(
        "Item Group",
        filters={
            "name": ["in", active_item_groups]
        },
        fields=["name", "item_group_name", "image"]
    )

    return item_group_details

@frappe.whitelist(allow_guest=True)
def get_item_detail(slug):
    items = frappe.get_all(
        "Item",
        filters={"slug": slug},
        fields=[
            "name", "item_name", "item_group", "slug",
            "image", "description", "business", "recomended", "delivery", "cod"
        ],
        limit=1
    )

    if not items:
        return None

    item = items[0]

    # --- AMBIL HARGA DASAR ---
    base_price = frappe.db.get_value("Price", {"item_name": item.name}, "price") or 0
    item["price"] = base_price

    # === TAMBAHAN KODE UNTUK DISKON ===
    item["discount_percent"] = 0
    item["discounted_price"] = base_price

    today = nowdate()
    # Cari apakah ada diskon aktif di toko ini
    active_discounts = frappe.get_all(
        "Discount",
        filters={
            "business": item.business,
            "start_date": ["<=", today],
            "end_date": [">=", today],
        },
        fields=["name", "amount"]
    )

    if active_discounts:
        discount_names = [d["name"] for d in active_discounts]
        # Cek apakah item ini masuk ke dalam daftar item diskon
        discount_item = frappe.get_all(
            "Item Discount",
            filters={
                "parent": ["in", discount_names],
                "item": item.name
            },
            fields=["parent"],
            limit=1
        )

        if discount_item:
            parent_discount = discount_item[0].parent
            for d in active_discounts:
                if d["name"] == parent_discount:
                    discount_amount = float(d["amount"] or 0)
                    item["discount_percent"] = discount_amount
                    item["discounted_price"] = round(base_price - (base_price * discount_amount / 100))
                    break
    # ==================================

    if item.item_group:
        group = frappe.db.get_value(
            "Item Group", item.item_group, ["item_group_name", "slug"], as_dict=True
        )
        item["item_group_name"] = group.item_group_name if group else None
        item["item_group_slug"] = group.slug if group and group.slug else None

    item["business"] = frappe.db.get_value(
        "Business",
        item.business,
        ["name", "business_name", "slug", "image", "phone_number"],
        as_dict=True
    )

    images = []
    if item.image:
        images.append({"image": item.image, "title": item.item_name})

    child_image_links = frappe.get_all(
        "Item Image Link",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["item_image"],
        order_by="idx asc"
    )

    for row in child_image_links:
        if row.item_image:
            img_detail = frappe.db.get_value(
                "Item Image",
                row.item_image,
                ["image", "title"],
                as_dict=True
            )
            if img_detail and img_detail.image:
                images.append({
                    "image": img_detail.image,
                    "title": img_detail.title or item.item_name
                })

    item["images"] = images

    child_components = frappe.get_all(
        "Item Component",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["component", "qty"],
        order_by="idx asc"
    )

    for c in child_components:
        if c.component:
            c["component_name"] = frappe.db.get_value("Component", c.component, "component_name")

    child_variants = frappe.get_all(
        "Item Variant",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["attribute", "value", "price_adjustment"],
        order_by="idx asc"
    )

    for v in child_variants:
        attr_label = frappe.db.get_value("Item Attribute", v.attribute, "attribute_name") or frappe.db.get_value("Item Attribute", v.attribute, "name")
        v["attribute_label"] = attr_label if attr_label else v.attribute

        val_label = frappe.db.get_value("Item Attribute Value", v.value, "value") or frappe.db.get_value("Item Attribute Value", v.value, "name")
        v["value_label"] = val_label if val_label else v.value

        v["price_adjustment"] = float(v.price_adjustment) if v.price_adjustment else 0

    item["variants"] = child_variants

    return item

@frappe.whitelist(allow_guest=True)
def get_discounted_items(slug):
    business_id = frappe.db.get_value("Business", {"slug": slug}, "name")
    if not business_id:
        return []

    today = nowdate()

    active_discounts = frappe.get_all(
        "Discount",
        filters={
            "business": business_id,
            "start_date": ["<=", today],
            "end_date": [">=", today],
        },
        fields=["name", "discount_name", "amount"],
    )

    if not active_discounts:
        return []

    discount_names = [d["name"] for d in active_discounts]

    discount_items = frappe.get_all(
        "Item Discount",
        filters={"parent": ["in", discount_names]},
        fields=["item", "parent"],
    )

    if not discount_items:
        return []

    discount_map = {}
    parent_amount_map = {d["name"]: d for d in active_discounts}
    for row in discount_items:
        if row.item:
            discount_map[row.item] = parent_amount_map.get(row.parent)

    item_ids = list(discount_map.keys())

    items = frappe.get_all(
        "Item",
        filters={
            "name": ["in", item_ids],
            "business": business_id,
        },
        fields=[
            "name", "item_name", "item_group", "image",
            "description", "business", "recomended", "slug","cod",
    "delivery",
        ],
    )

    if not items:
        return []

    item_docnames = [i["name"] for i in items]

    prices = frappe.get_all(
        "Price",
        filters={"item_name": ["in", item_docnames]},
        fields=["item_name", "price"],
    )
    price_map = {p["item_name"]: p["price"] for p in prices}

    group_ids = list(set([i["item_group"] for i in items if i.get("item_group")]))
    group_map = {}
    if group_ids:
        groups = frappe.get_all(
            "Item Group",
            filters={"name": ["in", group_ids]},
            fields=["name", "item_group_name", "slug"],
        )
        group_map = {g["name"]: g for g in groups}

    for item in items:
        base_price = price_map.get(item["name"]) or 0
        item["price"] = base_price

        group = group_map.get(item.get("item_group"))
        item["item_group_name"] = group["item_group_name"] if group else None
        item["item_group_slug"] = group["slug"] if group and group.get("slug") else None

        discount_info = discount_map.get(item["name"])
        if discount_info and base_price:
            discount_amount = float(discount_info["amount"] or 0)
            item["discount_percent"] = discount_amount
            item["discounted_price"] = round(base_price - (base_price * discount_amount / 100))
        else:
            item["discount_percent"] = 0
            item["discounted_price"] = base_price

    return items

@frappe.whitelist(allow_guest=True)
def track_item_click(slug):
    item_name = frappe.db.get_value("Item", {"slug": slug}, "name")

    if item_name:
        frappe.db.sql("""
            UPDATE `tabItem`
            SET `click` = IFNULL(`click`, 0) + 1
            WHERE `name` = %s
        """, (item_name,))
        frappe.db.commit()
        return True

    return False

@frappe.whitelist(allow_guest=True)
def create_sales_order(item, business, customer, custom_note=None):
    if not item or not business or not customer:
        frappe.throw("Data tidak lengkap untuk membuat pesanan.")

    so = frappe.new_doc("Sales Order")
    so.business = business
    so.item = item
    so.customer = customer
    so.custom_note = custom_note or ""
    so.order_date = nowdate()
    so.status = "Order Placed"
    so.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"name": so.name}
