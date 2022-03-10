$(function(){
  $.get('/graph', function(result) {
    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: [
        { selector: 'node[label = "Person"]',
          style: {'background-color': '#6FB1FC', 'label': 'data(name)'}
        },
        { selector: 'node[label = "Movie"]',
          style: {'background-color': '#F5A45D', 'label': 'data(title)'}
        },
        {
          selector: 'edge',
          style: {
            'width': 3,
            'line-color': 'blue',
            'target-arrow-color': 'red',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier'
          }
        }
      ],
      layout: { name: 'cose'},
      elements: result.elements
    });
  }, 'json');
});
