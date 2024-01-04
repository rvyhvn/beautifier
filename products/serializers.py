from marshmallow import Schema, fields as f


class CategorySchema(Schema):
    id = f.Int()
    name = f.Str()


class ProductSchema(Schema):
    id = f.Int()
    name = f.Str()
    description = f.Str()
    price = f.Int()
    stock = f.Int()
    # product_image = f.Str()
    category = f.Nested(CategorySchema)
