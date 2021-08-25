let browserWidth = window.innerWidth;
let viewportMeta = document.getElementsByName("viewport");

let content = viewportMeta["description"];

// viewportMeta.setAttribute('content', 'width=${browserWidth}')

console.log(viewportMeta);
console.log(content);
// console.log(browserWidth)