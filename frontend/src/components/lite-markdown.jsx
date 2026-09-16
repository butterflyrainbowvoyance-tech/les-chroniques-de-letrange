// A very small markdown-lite renderer that supports **bold** and *italic* only.
// Anything else is rendered as plain text within a <p>.

function renderInline(text) {
  const nodes = [];
  let rest = text;
  let key = 0;
  const patterns = [
    { re: /\*\*(.+?)\*\*/, tag: "strong" },
    { re: /\*(.+?)\*/, tag: "em" },
  ];

  while (rest.length > 0) {
    let earliest = null;
    for (const p of patterns) {
      const m = rest.match(p.re);
      if (m && (earliest == null || m.index < earliest.match.index)) {
        earliest = { match: m, tag: p.tag };
      }
    }
    if (!earliest) {
      nodes.push(rest);
      break;
    }
    const { match, tag } = earliest;
    if (match.index > 0) nodes.push(rest.slice(0, match.index));
    const Tag = tag;
    nodes.push(<Tag key={key++}>{match[1]}</Tag>);
    rest = rest.slice(match.index + match[0].length);
  }
  return nodes;
}

export default function LiteMarkdown({ children }) {
  if (!children) return null;
  return <p>{renderInline(children)}</p>;
}
