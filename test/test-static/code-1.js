$(function(){
  $.get('/graph', function(result) {   //用jQuery的$.get('/graph', function(result) {}, 'json')方法从app.py的’/graph’路径获得JSON数据存在result中。
    var style = [
      { selector: 'node[label = "Person"]', css: {'background-color': '#6FB1FC','content': 'data(name)'}},
      { selector: 'node[label = "Movie"]', css: {'background-color': '#F5A45D','content': 'data(title)'}},
      { selector: 'edge', css: {'content': 'data(relationship)', 'target-arrow-shape': 'triangle'}}  
    ];          //显示节点、关系内容

    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: style,
      layout: { name: 'cose', fit: false },      //{ name: 'grid'}    
      elements: result.elements             //elements: result.elements把result里的elements复给elements属性
    });
  }, 'json');  
});






//code.js


$(function(){
  $.get('/graph', function(result_nr) {   //用jQuery的$.get('/graph', function(result_nr) {}, 'json')方法从app.py的’/graph’路径获得JSON数据存在result_nr中。
    var style = [
      { selector: 'node[label = "Person"]', css: {'background-color': '#6FB1FC'}},
      { selector: 'node[label = "Movie"]', css: {'background-color': '#F5A45D'}},
    ];          //显示节点、关系内容

    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: style,
      layout: { name: 'cose', fit: false },      //{ name: 'grid'}    
      elements: result_nr.elements             //elements: result.elements把result里的elements赋给elements属性
    });
  }, 'json');  
});









$(function(){
  $.get('/graph', function(result_nr) {   //用jQuery的$.get('/graph', function(result_nr) {}, 'json')方法从app.py的’/graph’路径获得JSON数据存在result_nr中。
    var style = [
      { selector: 'node[label = "壁画"]', css: {'background-color': '#4169E1'}},
      { selector: 'node[label = "主题"]', css: {'background-color': '#FFD700'}},
      { selector: 'node[label = "布局"]', css: {'background-color': '#FA8072'}},     
      { selector: 'node[label = "朝代"]', css: {'background-color': '#EE82EE'}},
      { selector: 'node[label = "洞窟"]', css: {'background-color': '#F4A460'}},
      { selector: 'node[label = "类型"]', css: {'background-color': '#3CB371'}},
      
      { selector: 'edge', css: {'content': 'data(relationship)', 'target-arrow-shape': 'triangle'}} 
  
   
      
    ];          //显示节点、关系内容

    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: style,
      layout: { name: 'cose', fit: false },      //{ name: 'grid'}    
      elements: result_nr.elements             //elements: result.elements把result里的elements赋给elements属性
    });
  }, 'json');  
});

