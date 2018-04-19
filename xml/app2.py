from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {
                "keywords":"路思義教堂",
                "limit":1000,
                "print_urls":True,
                "output_directory":"./1410332003",
                "chromedriver":"./chromedriver"
            }   
response.download(arguments)
