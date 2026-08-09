import frappe

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
def get_items(slug, recomended=None, item_group=None):
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

    for item in items:
        item["price"] = price_map.get(item["name"])

    return items

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
            "image", "description", "business", "recomended"
        ],
        limit=1
    )

    if not items:
        return None

    item = items[0]

    # Price
    item["price"] = frappe.db.get_value("Price", {"item_name": item.name}, "price")

    # Item Group label
    if item.item_group:
        item["item_group_name"] = frappe.db.get_value(
            "Item Group", item.item_group, "item_group_name"
        )

    # Business + phone_number
    item["business"] = frappe.db.get_value(
        "Business",
        item.business,
        ["name", "business_name", "slug", "image", "phone_number"],
        as_dict=True
    )

    # Images: gambar utama di index 0, lalu child table "Item Image"
    images = []
    if item.image:
        images.append(item.image)

    child_image_links = frappe.get_all(
        "Item Image Link",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["item_image"],
        order_by="idx asc"
    )

    for row in child_image_links:
        if row.item_image:
            img_file = frappe.db.get_value("Item Image", row.item_image, "image")
            if img_file:
                images.append(img_file)

    item["images"] = images

    # Attributes: kelompokkan per nama atribut -> list of values
    child_attributes = frappe.get_all(
        "Item Attribute",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["attribute", "attribute_value"],
        order_by="idx asc"
    )

    attributes = {}
    for row in child_attributes:
        if not row.attribute or not row.attribute_value:
            continue
        attributes.setdefault(row.attribute, [])
        if row.attribute_value not in attributes[row.attribute]:
            attributes[row.attribute].append(row.attribute_value)

    item["attributes"] = attributes

    # Components: Isi Paket
    child_components = frappe.get_all(
        "Item Component",
        filters={"parent": item.name, "parenttype": "Item"},
        fields=["component", "qty"],
        order_by="idx asc"
    )

    for c in child_components:
        if c.component:
            c["component_name"] = frappe.db.get_value("Component", c.component, "component_name")

    item["components"] = child_components
    return item
