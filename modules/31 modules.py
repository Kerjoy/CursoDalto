#import module an ranaming
#import greatings_module as mod
#specific import module
#from greating_module import * #imports all in the module considered bad practice
from greatings_module import greatings as gt, greatings_spanish as gts

greating_result = gt("taquito")
greating_result = gts("taquito")

print(greating_result)
print(greating_result)

print(gt.__name__,gts.__name__)

#print(dir(gt))
#print (type(greatings_module)) return this <class 'module'>