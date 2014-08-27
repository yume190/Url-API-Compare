# -*- coding: utf-8 -*-
from BusAPI import *


oldJSONAPIList = [
#1
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetProvider.json",[],["ID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetProvider.json",[],["ID"]),
#2
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetRoute.json",[],["ProviderId","ID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetRoute.json",[],["ProviderId","ID"]),
#4
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetStop.json?routeIds=30",[],["GoBack","seqNo"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetStop.json?routeIds=30",[],["GoBack","seqNo"]),
#6
BusAPIOld("http://192.168.10.245/xmlbus4/GetBusData.json?routeIds=30",[],["BusID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/GetBusData.json?routeIds=30",[],["BusID"]),
#5
BusAPIOld("http://192.168.10.245/xmlbus4/GetEstimateTime.json?routeIds=30",["30"],["GoBack","seqNo"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/GetEstimateTime.json?routeIds=30",["30"],["GoBack","seqNo"])
]

newJSONAPIList = [
#1
BusAPINew("http://192.168.10.245/xml/StaticData/GetProvider.json",[],["ID"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetProvider.json",[],["ID"]),
#2
BusAPINew("http://192.168.10.245/xml/StaticData/GetRoute.json",[],["ProviderId","ID"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetRoute.json",[],["ProviderId","ID"]),
#4
BusAPINew("http://192.168.10.245/xml/StaticData/GetStop.json?routeIds=30",[],["GoBack","seqNo"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetStop.json?routeIds=30",[],["GoBack","seqNo"]),
#6
BusAPINew("http://192.168.10.245/xml/GetBusData.json?routeIds=30",[],["BusID"]),
BusAPINew("http://192.168.10.245/xml/en/GetBusData.json?routeIds=30",[],["BusID"]),
#5
BusAPINew("http://192.168.10.245/xml/GetEstimateTime.json?routeIds=30",["30"],["GoBack","seqNo"]),
BusAPINew("http://192.168.10.245/xml/en/GetEstimateTime.json?routeIds=30",["30"],["GoBack","seqNo"])
]

oldXMLAPIList = [
#1.業者
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetProvider.xml",["BusDynInfo","BusInfo","Provider"],["@ID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetProvider.xml",["BusDynInfo","BusInfo","Provider"],["@ID"]), #（台中英文不完整）
#2.路線
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetRoute.xml",["BusDynInfo","BusInfo","Route"],["@ProviderId","@ID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetRoute.xml",["BusDynInfo","BusInfo","Route"],["@ProviderId","@ID"]),
#3.車輛類別
#"http://192.168.10.245/tcbus2/lfv_n.php",
#4.站牌
BusAPIOld("http://192.168.10.245/xmlbus4/StaticData/GetStop.xml?routeIds=30",["BusDynInfo","BusInfo","Stop"],["@GoBack","@seqNo"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/StaticData/GetStop.xml?routeIds=30",["BusDynInfo","BusInfo","Stop"],["@GoBack","@seqNo"]),
#5.預估到站
BusAPIOld("http://192.168.10.245/xmlbus4/GetEstimateTime.xml?routeIds=30",["BusDynInfo","BusInfo","Route","EstimateTime"],["@GoBack","@seqNo"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/GetEstimateTime.xml?routeIds=30",["BusDynInfo","BusInfo","Route","EstimateTime"],["@GoBack","@seqNo"]),
#6.車機資訊
BusAPIOld("http://192.168.10.245/xmlbus4/GetBusData.xml?routeIds=30",["BusDynInfo","BusInfo","BusData"],["@BusID"]),
BusAPIOld("http://192.168.10.245/xmlbus4/en/GetBusData.xml?routeIds=30",["BusDynInfo","BusInfo","BusData"],["@BusID"])
]

newXMLAPIList = [
#1.業者
BusAPINew("http://192.168.10.245/xml/StaticData/GetProvider.xml",["BusDynInfo","BusInfo","Provider"],["@ID"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetProvider.xml",["BusDynInfo","BusInfo","Provider"],["@ID"]), #（台中英文不完整）
#2.路線
BusAPINew("http://192.168.10.245/xml/StaticData/GetRoute.xml",["BusDynInfo","BusInfo","Route"],["@ProviderId","@ID"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetRoute.xml",["BusDynInfo","BusInfo","Route"],["@ProviderId","@ID"]),
#3.車輛類別
#"http://192.168.10.245/tcbus2/lfv_n.php",
#4.站牌
BusAPINew("http://192.168.10.245/xml/StaticData/GetStop.xml?routeIds=30",["BusDynInfo","BusInfo","Stop"],["@GoBack","@seqNo"]),
BusAPINew("http://192.168.10.245/xml/en/StaticData/GetStop.xml?routeIds=30",["BusDynInfo","BusInfo","Stop"],["@GoBack","@seqNo"]),
#5.預估到站
BusAPINew("http://192.168.10.245/xml/GetEstimateTime.xml?routeIds=30",["BusDynInfo","BusInfo","Route","EstimateTime"],["@GoBack","@seqNo"]),
BusAPINew("http://192.168.10.245/xml/en/GetEstimateTime.xml?routeIds=30",["BusDynInfo","BusInfo","Route","EstimateTime"],["@GoBack","@seqNo"]),
#6.車機資訊
BusAPINew("http://192.168.10.245/xml/GetBusData.xml?routeIds=30",["BusDynInfo","BusInfo","BusData"],["@BusID"]),
BusAPINew("http://192.168.10.245/xml/en/GetBusData.xml?routeIds=30",["BusDynInfo","BusInfo","BusData"],["@BusID"])
]

oldAPIList = oldJSONAPIList + oldXMLAPIList
newAPIList = newJSONAPIList + newXMLAPIList
