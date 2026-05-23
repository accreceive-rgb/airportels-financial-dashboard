process.env.NODE_PATH = "C:\\Users\\AI-IT-386\\AppData\\Roaming\\npm\\node_modules";
require("module").Module._initPaths();
const { PDFParse } = require("pdf-parse");
const fs = require("fs");
const buf = fs.readFileSync("C:/Users/AI-IT-386/Downloads/สลิปโอนจ่าย 07.05.2026.pdf");
const parser = new PDFParse();
parser.parse(buf, {max: 3}).then(data => {
  process.stdout.write("Total pages: " + data.numpages + "\n");
  process.stdout.write("Text:\n" + data.text.slice(0, 3000) + "\n");
}).catch(e => process.stderr.write("Error: " + e.message + "\n" + e.stack + "\n"));
