import json
from openfood import QueryError

class ProductBuilder:
    
    def __init__(self, product):
        self.name = ''
        self.images = []
        # Get name
        try:
            self.name = ProductBuilder.get_valid_name(product)
        except QueryError as err:
            self.name = 'None'
            print(err.message)
        # Get images
        try:
            self.images = ProductBuilder.get_valid_image(product)
        except QueryError as err:
            print(err.message)
        # Get barcode
        self.barcode = ProductBuilder.get_valid_barcode(product)
        # Get composition
        self.nutrients = ProductBuilder.get_valid_nutrient(product)
        self.raw = product
        
    def get_json(self):
        res_dict = {}
        res_dict['name'] = self.name
        res_dict['barcode'] = self.barcode
        res_dict['images'] = self.images
        res_dict['nutrients'] = self.nutrients
        return res_dict
    
    @staticmethod
    def clean_data(res_tab):
        res = []
        for i, product in enumerate(res_tab):
            product_build = ProductBuilder(product)
            res.append(product_build.get_json()) 
        return res
    
    @staticmethod
    def get_valid_nutrient(product):
        """
        Get valid nutrient
        """
        nutrient_tab = [];
        try:
            nutirents = product['_source']['nutrients']
            for nutirent in nutirents:
                try:
                    name = nutirent['name_fr']
                    per_hundred = nutirent['per_hundred']
                    nutrient_tab.append({'name':name, 'per_hundred': per_hundred})
                except:
                    pass
        except KeyError:
            pass
        
        return nutrient_tab
        
    @staticmethod
    def get_valid_barcode(product):
        """
        Get valid barcode of product
        """
        try:
            return product['_source']['barcode']
        except KeyError:
            pass
        return '0'
    
    @staticmethod
    def get_valid_name(product):
        """
        Get valid display name of product
        """
        name_fr = None
        try:
            name_fr = product['_source']['name_fr']
        except KeyError:
            pass
        if(name_fr is not None):
            return name_fr
        else:
            try:
                name_fr = product['_source']['name_translations']['fr']
                return name_fr
            except KeyError:
                pass
            try:
                name_fr = product['_source']['ingredients_translations']['fr']
                return name_fr
            except KeyError:
                raise QueryError(QueryError.NO_NAME, 'No name found')
        return 'No name'
    
    @staticmethod
    def get_valid_image(product, size='large'):
        """
        Get valid display name of product
        """
        img_valid_url = []
        try:
            imgs = product['_source']['images']
            for img in imgs:
                img_valid_url.append(img['data'][size]['url'])
        except KeyError:
            pass
        
        return img_valid_url
