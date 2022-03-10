$(function(){
  $.get('/graph', function(result_nr) {   //用jQuery的$.get('/graph', function(result_nr) {}, 'json')方法从app.py的’/graph’路径获得JSON数据存在result_nr中。
   
    var cy = cytoscape({
      container: document.getElementById('cy'),
      style:  [                                          //显示节点、关系内容
        { selector: 'node[label = "壁画"]',
          style: {'background-color': '#4169E1', 'label': 'data(name)'}
        },
        { selector: 'node[label = "主题"]',
          style: {'background-color': '#FFCC22', 'label': 'data(name)'}
        },
         { selector: 'node[label = "布局"]',
          style: {'background-color': '#77FFCC', 'label': 'data(name)'}
        },
        { selector: 'node[label = "朝代"]',
          style: {'background-color': '#FA8072', 'label': 'data(name)'}
        },
         { selector: 'node[label = "洞窟"]',
          style: {'background-color': '#D2B48C', 'label': 'data(name)'}
        },
        { selector: 'node[label = "类型"]',
          style: {'background-color': '#3CB371', 'label': 'data(name)'}
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'line-color': '#778899',
            'target-arrow-color': '#778899',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'content': 'data(relationship)'
          }
        }
      ],
      layout:{ name: 'circle'} ,      //{ name: 'grid'}   or   { name: 'cose', fit: false }  circle \ random \breadthfirst\ preset
      elements: result_nr.elements             //elements: result.elements把result里的elements赋给elements属性
    });
  }, 'json');  
});

