# coding = utf-8

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os


class MeiZiTuImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["url"]
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        if (item["type"] == 'meizitu'):
            image_paths = [x["path"] for ok, x in result if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            os.rename(self.IMAGES_STORE + "/" + image_paths[0],
                      self.IMAGES_STORE + "MeiZiTu/Images/" + item["title"] + ".jpg")
            item["image_url"] = self.IMAGES_STORE + "MeiZiTu/Images/" + item["title"]
        if (item["type"] == 'guoji'):
            image_paths = [x["path"] for ok, x in result if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            os.rename(self.IMAGES_STORE + "/" + image_paths[0],
                      self.IMAGES_STORE + "GuoJi/Images/" + item["title"] + ".jpg")
            item["image_url"] = self.IMAGES_STORE + "GuoJi/Images/" + item["title"]

        return item
