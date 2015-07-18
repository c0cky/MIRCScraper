# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class FSImagesStoreChangeableDirectory(FSImagesStore):

    def persist_image(self, key, image, buf, info,append_path):
        absolute_path = self._get_filesystem_path(append_path+'/'+key)
	self._mkdir(os.path.dirname(absolute_path), info)
	print absolute_path
	image.save(absolute_path)

class ProjectPipeline(ImagesPipeline):

    def __init__(self):
        super(ImagesPipeline, self).__init__()
        store_uri = settings.IMAGES_STORE
        if not store_uri:
            raise NotConfigured
        self.store = FSImagesStoreChangeableDirectory(store_uri)
