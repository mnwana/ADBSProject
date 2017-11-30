var app = angular.module('myApp', []);
app.controller('ctrl', function($http, $scope) {
	
	var self = this;
	self.searchText = "";
	self.index = "politics";
	self.vizType = "";
	self.visuals = [];
	
	
	self.fuzzy = false;
	self.retweets = false;
	
	self.showVis = false;
	
	self.urls = [];
	
	self.countURL = "https://iad1-11037-kibana.es.objectrocket.com:21037/app/kibana#/visualize/edit/Global-Tweet-Count-politics?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-12h,mode:quick,to:now))&_a=(filters:!(),linked:!f,query:(query_string:(query:'QUERYHERE')),uiState:(vis:(defaultColors:('0+-+100':'rgb(0,104,55)'))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Tweet+Count'),schema:metric,type:count)),listeners:(),params:(addLegend:!f,addTooltip:!t,gauge:(autoExtend:!f,backStyle:Full,colorSchema:'Green+to+Red',colorsRange:!((from:0,to:100)),gaugeColorMode:None,gaugeStyle:Full,gaugeType:Metric,invertColors:!f,labels:(color:black,show:!t),orientation:vertical,percentageMode:!f,scale:(color:%23333,labels:!f,show:!f,width:2),style:(bgColor:!f,fontSize:20,labelColor:!f,subText:''),type:simple,useRange:!f,verticalSplit:!f),type:gauge),title:'Global+Tweet+Count',type:metric))";
	self.mapURL = "https://iad1-11037-kibana.es.objectrocket.com:21037/app/kibana#/visualize/edit/AWAI92jzmQ7NZ-r8v9wR?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-12h,mode:quick,to:now))&_a=(filters:!(),linked:!f,query:(query_string:(analyze_wildcard:!t,query:'QUERYHERE')),uiState:(mapCenter:!(35.17380831799959,-6.591796875),mapZoom:3),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(autoPrecision:!t,field:coordinates.coordinates,precision:4,useGeocentroid:!t),schema:segment,type:geohash_grid)),listeners:(),params:(addTooltip:!t,heatBlur:'24',heatMaxZoom:'12',heatMinOpacity:'1',heatRadius:'17',isDesaturated:!t,legendPosition:bottomright,mapCenter:!(0,0),mapType:Heatmap,mapZoom:2,type:tile_map,wms:(enabled:!f,options:(attribution:'Maps+provided+by+USGS',format:image%2Fpng,layers:'0',styles:'',transparent:!t,version:'1.3.0'),url:'https:%2F%2Fbasemap.nationalmap.gov%2Farcgis%2Fservices%2FUSGSTopo%2FMapServer%2FWMSServer')),title:'Number+of+Tweets+by+Location',type:tile_map))";
	self.placesURL = "https://iad1-11037-kibana.es.objectrocket.com:21037/app/kibana#/visualize/edit/%5BLinegraph%5D-Tweets-count-by-top-5-location-politics?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-12h,mode:quick,to:now))&_a=(filters:!(),linked:!f,query:(query_string:(query:'QUERYHERE')),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Number+of+Tweets'),schema:metric,type:count),(enabled:!t,id:'3',params:(field:user.location,order:desc,orderBy:'1',size:5),schema:group,type:terms),(enabled:!t,id:'2',params:(customInterval:'2h',customLabel:'Time+(30+minute+buckets)',extended_bounds:(),field:'@timestamp',interval:auto,min_doc_count:1),schema:segment,type:date_histogram)),listeners:(),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(text:'Time+(30+minute+buckets)'),type:category)),defaultYExtents:!f,drawLinesBetweenPoints:!t,grid:(categoryLines:!f,style:(color:%23eee)),interpolate:linear,legendPosition:right,radiusRatio:9,scale:linear,seriesParams:!((data:(id:'1',label:'Number+of+Tweets'),drawLinesBetweenPoints:!t,interpolate:linear,mode:stacked,radiusRatio:9,show:true,showCircles:!t,type:line,valueAxis:ValueAxis-1)),setYExtents:!f,shareYAxis:!t,showCircles:!t,smoothLines:!f,times:!(),type:line,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(defaultYExtents:!f,mode:normal,setYExtents:!f,type:linear),show:!t,style:(),title:(text:'Number+of+Tweets'),type:value)),yAxis:()),title:'Live+Tweets+Count+by+Top+10+Locations',type:line))";
	self.mhastagURL = "https://iad1-11037-kibana.es.objectrocket.com:21037/app/kibana#/visualize/edit/AWAKF8AJmQ7NZ-r8v9wW?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-12h,mode:quick,to:now))&_a=(filters:!(),linked:!f,query:(query_string:(analyze_wildcard:!t,query:'lang:en')),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(customInterval:'2h',extended_bounds:(),field:'@timestamp',interval:auto,min_doc_count:1),schema:segment,type:date_histogram),(enabled:!t,id:'3',params:(field:entities.hashtags.text,order:desc,orderBy:'1',size:15),schema:group,type:terms)),listeners:(),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(text:'@timestamp+per+3+hours'),type:category)),grid:(categoryLines:!f,style:(color:%23eee)),legendPosition:right,seriesParams:!((data:(id:'1',label:Count),drawLinesBetweenPoints:!t,mode:stacked,show:true,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Count),type:value))),title:'Popular+Hashtags',type:histogram))"
	self.mhashCloudURL = "https://iad1-11037-kibana.es.objectrocket.com:21037/app/kibana#/visualize/edit/AWAKLrhumQ7NZ-r8v9wX?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now%2Fw,mode:quick,to:now%2Fw))&_a=(filters:!(),linked:!f,query:(query_string:(query:'lang:en')),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(field:entities.hashtags.text,order:desc,orderBy:'1',size:20),schema:segment,type:terms)),listeners:(),params:(maxFontSize:73,minFontSize:18,orientation:single,scale:log,type:tagcloud),title:'Hashtag+Cloud',type:tagcloud))"

	self.ops = [];
	self.counter = {'url':self.countURL, 'height':200, 'width':200}
	self.ops.append({"index":"politics", "type":"map", "url":self.mapURL})
	self.ops.append({"index":"politics", "type":"map", "url":self.placesURL})
	self.ops.append({"index":"movies", "type":"hash", "url":self.mhastagURL})
	self.ops.append({"index":"movies", "type":"hash", "url":self.mapURL})
	self.ops.append({"index":"politics", "type":"map", "url":self.mapURL})
	self.visURL = "";
	
	self.viz = [];
	
self.selectViz = function(type){
	
	self.viz = [];
	
	if(self.fuzzy){
		
		self.searchText = self.searchText.replace(" ", "~ ") + "~";
		
	}
	
	self.viz.push({'url':self.counter['url'].replace("QUERYHERE", encodeURIComponent(self.searchText)), 'height':self.counter['height'], 'width':self.counter['width']})
	
	
	for(var i=0; i < self.ops.length; i++){
		
		if(self.ops[i][index] == self.index){
			self.viz.push({'url':self.ops[i]['url'].replace("QUERYHERE", encodeURIComponent(self.searchText)), 'height':self.ops[i]['height'], 'width':self.ops[i]['width']})
		}
		
	}
	
	
	self.showVis = true;

	
}




	
});

app.filter('trusted', ['$sce', function ($sce) {
   return $sce.trustAsResourceUrl;
}]);