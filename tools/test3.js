process.env.NODE_PATH = "C:\\Users\\AI-IT-386\\AppData\\Roaming\\npm\\node_modules";
require("module").Module._initPaths();
const { PDFParse } = require("pdf-parse");
const fs = require("fs");
const buf = fs.readFileSync("C:/Users/AI-IT-386/Downloads/สลิปโอนจ่าย 07.05.2026.pdf");
const parser = new PDFParse();
// Parse only 3 pages, with custom page renderer to see raw content
const options = {
  max: 3,
  pagerender: function(pageData) {
    return pageData.getTextContent().then(tc => {
      const items = tc.items || [];
      if (items.length > 0) {
        return items.map(i => i.str).join(" ");
      }
      return "[NO_TEXT_PAGE]";
    });
  }
};
parser.parse(buf, options).then(data => {
  console.log("Pages:", data.numpages);
  console.log("Text extracted:", JSON.stringify(data.text.slice(0, 2000)));
}).catch(e => console.error("ERR:", e.message));
