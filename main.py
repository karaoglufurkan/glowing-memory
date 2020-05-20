import os

from categorization import Categorization

cat = Categorization(os.path.join(os.getcwd(), "source_folder"), os.path.join(os.getcwd(), "target_folder"))

cat.create_folders()
cat.categorize()