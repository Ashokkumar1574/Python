from PIL import Image

def merge_images(image1_path, image2_path, output_path):
   
    image1 = Image.open(//image1_path)
    image2 = Image.open(//image2_path)
    image2 = image2.resize(image1.size)
    merged_image = Image.blend(image1, image2, alpha=0.5)

    merged_image.save(output_path)
image1_path = "image1.jpg"//img 1 path
image2_path = "image2.jpg"// imge 2 path
output_path = "merged_image.jpg"// resultant img path

merge_images(image1_path, image2_path, output_path)
