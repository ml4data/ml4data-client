from ml4data.base import ML4DataClient
from PIL import Image
from io import BytesIO

class VisionClient(ML4DataClient):
    base_url = ML4DataClient.base_url + '/vision'

    def _send_image(self, endpoint, img=None, url=None):
        if (img is None and url is None) or (img is not None and url is not None):
            raise ValueError("Pass either a path, file handler, Pillow image or url as argument")

        if img is not None:
            if isinstance(img, str):
                with open(img, 'rb') as fp:
                    r = self._post(endpoint=endpoint,
                                   files={'file': fp})
            elif isinstance(img, Image.Image):
                b = BytesIO()
                img.save(b, 'png')
                b.seek(0)
                r = self._post(endpoint=endpoint,
                               files={'file': b})
            else: # file-like
                r = self._post(endpoint=endpoint,
                               files={'file': img})
        else: # url is not None:
            r = self._get(endpoint=endpoint,
                          params={'url': url})
        return r

    def detect_object(self, img=None, url=None):
        """ Detect objects in an image

        Pass either one of img, url as arguments

        Params:
            img (str, file-like or PIL.Image): Path to the image, or file
                handler of the opened image, or Pillow image
            url (str): Image url
        """
        return self._send_image('/object-detection',
                                img=img,
                                url=url)

    def detect_facemask(self, img=None, url=None):
        """ Detect face maks in an image

        Pass either one of path, fp, img, url as arguments

        Params:
            img (str, file-like or PIL.Image): Path to the image, or file
                handler of the opened image, or Pillow image
            url (str): Image url
        """
        return self._send_image('/facemask-detection',
                                img=img,
                                url=url)

    def classify_product(self, img=None, url=None):
        """ Classify the main product in an image

        Pass either one of path, fp, img, url as arguments

        Params:
            img (str, file-like or PIL.Image): Path to the image, or file
                handler of the opened image, or Pillow image
            url (str): Image url
        """
        return self._send_image('/products',
                                img=img,
                                url=url)

    def ocr(self, img=None, url=None):
        """ Extract text from an image

        Pass either one of path, fp, img, url as arguments

        Params:
            img (str, file-like or PIL.Image): Path to the image, or file
                handler of the opened image, or Pillow image
            url (str): Image url
        """
        return self._send_image('/ocr',
                                img=img,
                                url=url)

    def colors(self, img=None, url=None):
        """ Find main colors in an image

        Pass either one of path, fp, img, url as arguments

        Params:
            img (str, file-like or PIL.Image): Path to the image, or file
                handler of the opened image, or Pillow image
            url (str): Image url
        """
        return self._send_image('/colors',
                                img=img,
                                url=url)
