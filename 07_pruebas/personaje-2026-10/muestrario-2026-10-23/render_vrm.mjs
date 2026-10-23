// Render del muestrario VRM: fotograma a fotograma en Chromium sin GPU.
// Uso (desde una carpeta con node_modules de three, @pixiv/three-vrm y playwright-core, más
// avatar.vrm, boca.json y escena_vrm.html): node render_vrm.mjs <modo> <w> <h> <n_fotogramas> <salida_dir>
import { chromium } from 'playwright-core';
import { createServer } from 'node:http';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { extname, join } from 'node:path';
const [modo = 'retrato', w = '540', h = '960', n = '350', out = 'frames'] = process.argv.slice(2);
const TIPOS = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.vrm': 'model/gltf-binary' };
const srv = createServer(async (rq, rs) => {
  try { const p = join(process.cwd(), decodeURIComponent(rq.url.split('?')[0])); rs.writeHead(200, { 'content-type': TIPOS[extname(p)] || 'application/octet-stream' }); rs.end(await readFile(p)); }
  catch { rs.writeHead(404); rs.end(); }
}).listen(0);
const port = srv.address().port;
const nav = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const pg = await nav.newPage({ viewport: { width: +w, height: +h } });
pg.on('console', m => console.log('[pagina]', m.text())); pg.on('pageerror', e => console.log('[error]', e.message));
await pg.goto(`http://localhost:${port}/escena_vrm.html?modo=${modo}&w=${w}&h=${h}`);
await pg.waitForFunction('window.listo === true', null, { timeout: 120000 });
await mkdir(out, { recursive: true });
const t0 = Date.now();
for (let i = 0; i < +n; i++) {
  const url = await pg.evaluate(k => window.frame(k), i);
  await writeFile(join(out, `f${String(i).padStart(4, '0')}.png`), Buffer.from(url.split(',')[1], 'base64'));
}
const s = (Date.now() - t0) / 1000;
console.log(`render ${n} fotogramas en ${s.toFixed(1)} s (${(s / +n * 1000).toFixed(0)} ms/fotograma)`);
await nav.close(); srv.close();
