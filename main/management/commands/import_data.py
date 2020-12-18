from collections import Counter
import csv
import os.path
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.template.defaultfilters import slugify
from main import models

class Command(BaseCommand):
    help = 'Import products in BookTime'

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=open)
        parser.add_argument("image_basedir", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Importing products")
        c = Counter()
        reader = csv.DictReader(options.pop("csvfile"))
        for row in reader:
            product, created = models.Product.objects.get_or_create(
                name=row["name"], 
                price=row["price"],
                description = row["description"],
                slug = slugify(row["name"])
            )
    
            for import_tag in row["tags"].split("|"):
                tag, tag_created = models.ProductTag.objects.get_or_create(
                    name = import_tag
                )
                product.tags.add(tag)
                c["tags"]+=1
                if tag_created:
                    c["tags_created"]+=1

            for import_image in row["image_filename"].splitlines():
                with open(
                    os.path.join(
                        options["image_basedir"],
                        import_image,
                    ),
                    "rb",
                ) as f:
                    image, image_created = models.ProductImage.objects.get_or_create(
                        product = product,
                        image=ImageFile(
                            f, name=import_image
                        )
                    )
                    c["images"]+=1
                    if image_created:
                        c["images_created"]+=1

            c["products"]+=1
            if created:
                c["products_created"]+=1
        
        self.stdout.write(
            "Product processed=%d (created=%d)"
            % (c["products"], c["products_created"])
        )

        self.stdout.write(
            "Tags processed=%d (created=%d)"
            % (c["tags"], c["tags_created"])
        )
        self.stdout.write(
            "Image processed=%d (created=%d)" % (c["images"], c["images_created"]))

                
                
        


