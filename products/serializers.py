from marshmallow import Schema, fields as f


class CategorySchema(Schema):
    id = f.Int()
    category_name = f.Str()


class ProductSchema(Schema):
    id = f.Int()
    product_name = f.Str()
    product_description = f.Str()
    product_price = f.Int()
    product_stock = f.Int()
    # product_image = f.Str()
    category = f.Nested(CategorySchema)
