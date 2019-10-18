from django.contrib.gis.serializers.geojson import Serializer
from django.db.models import Manager
# FYI: It can be any of the following as well:
# from django.core.serializers.pyyaml import Serializer
# from django.core.serializers.python import Serializer
# from django.core.serializers.json import Serializer

JSON_ALLOWED_OBJECTS = (dict,list,tuple,str,int,bool)

# This custom serializer is for accessing other relating model 
# fields

class CustomSerializer(Serializer):

    def end_object(self, obj):
        for field in self.selected_fields:
            if field == 'pk':
                continue
            elif field in self._current.keys():
                continue
            else:
                try:
                    if '__' in field:
                        fields = field.split('__')
                        value = obj
                        for f in fields:
                            value = getattr(value, f)
                        if value != obj:
                            self._current[field] = value

                except AttributeError:
                    pass
        super(CustomSerializer, self).end_object(obj)