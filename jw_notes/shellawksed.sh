#!/usr/bin/env bash

// export {Router, Route, match,RoutingContext,IndexRoute,Link,browserHistory as HistoryHandle } from 'dva/router';
export {Router, Route,match,RoutingContext, IndexRoute,Link,hashHistory as HistoryHandle } from 'dva/router';
// export {Router, Route, match,RoutingContext,IndexRoute,Link,memoryHistory as HistoryHandle } from 'react-router';

 sed -i '1 s/\/\///g' router_helper.js |sed 's/^[ \t]*//g'|sed '2 s/^/\/\//g'
 sed -i  '2 s/^/\/\//g' router_helper.js |sed '1 s/\/\///g'
 cat router_helper.js |sed -i '1 s/\/\///g'|sed -i  '2 s/^/\/\//g'

 sed -i '1 s/\/\///g' router_helper.js
 sed -i '2 s/^/\/\//g' router_helper.js
 sed -i 's/^[ \t]*//g' router_helper.js


