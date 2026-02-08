(function () {
  const container = document.getElementById("knowledge-graph");
  if (!container) return;

    const dataEl = document.getElementById("graph-data");
    const data = JSON.parse(dataEl.textContent);
    initGraph(data);
  function initGraph(data) {
    const nodes = new vis.DataSet(
      data.nodes.map(n => ({
        id: n.id,
        label: n.label,
        group: n.kind,
        title: n.description || "",
        color: nodeColor(n.kind),
        font: { color: "#ffffff" }
      }))
    );

    const edges = new vis.DataSet(
      data.edges.map((e, i) => ({
        id: i,
        from: e.from,
        to: e.to,
        arrows: "to",
        label: e.relation,
        color: { opacity: 0.6 }
      }))
    );

    const network = new vis.Network(container, { nodes, edges }, networkOptions());

    network.on("selectNode", params => {
      const selected = params.nodes[0];
      const connected = network.getConnectedNodes(selected);

      nodes.forEach(node => {
        nodes.update({ id: node.id, opacity: selected === node.id || connected.includes(node.id) ? 1 : 0.2 });
      });

      edges.forEach(edge => {
        edges.update({
          id: edge.id,
          color: { opacity: edge.from === selected || edge.to === selected || (connected.includes(edge.from) && connected.includes(edge.to)) ? 0.8 : 0.1 }
        });
      });
    });

    network.on("deselectNode", () => {
      nodes.forEach(node => nodes.update({ id: node.id, opacity: 1 }));
      edges.forEach(edge => edges.update({ id: edge.id, color: { opacity: 0.6 } }));
    });
  }

  function nodeColor(kind) {
    return {
      question: "#1e88e5",
      answer: "#43a047",
      outcome: "#f9a825"
    }[kind] || "#9e9e9e";
  }

  function networkOptions() {
    return {
      autoResize: true,
      layout: { improvedLayout: true },
      physics: { stabilization: false },
      interaction: { hover: true },
      nodes: { shape: "dot", size: 14, font: { size: 14 } },
      edges: { smooth: true, font: { size: 10, align: "middle" } }
    };
  }
})();
