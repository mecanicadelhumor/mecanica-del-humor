// Pista de boca determinista a partir del audio (sin red, sin modelos):
// energía por fotograma -> apertura; cruce por cero (brillo del sonido) -> qué vocal.
// Uso: node boca.mjs audio.mp3 segundos fps > boca.json
import { execFileSync } from 'node:child_process';
const [audio, dur = '14', fps = '25'] = process.argv.slice(2);
const SR = 16000;
const raw = execFileSync('ffmpeg', ['-v', 'error', '-t', dur, '-i', audio, '-ac', '1', '-ar', String(SR), '-f', 's16le', '-'], { maxBuffer: 1 << 28 });
const s = new Int16Array(raw.buffer, raw.byteOffset, raw.length / 2);
const hop = SR / Number(fps), n = Math.floor(s.length / hop);
const rms = [], zcr = [];
for (let i = 0; i < n; i++) {
  let e = 0, z = 0;
  for (let j = i * hop + 1; j < (i + 1) * hop; j++) { e += s[j] * s[j]; if ((s[j] >= 0) !== (s[j - 1] >= 0)) z++; }
  rms.push(Math.sqrt(e / hop)); zcr.push(z / hop);
}
const sorted = [...rms].sort((a, b) => a - b), p95 = sorted[Math.floor(sorted.length * 0.95)], floor = sorted[Math.floor(sorted.length * 0.25)];
const frames = rms.map((r, i) => {
  let a = Math.max(0, Math.min(1, (r - floor) / (p95 - floor)));
  a = Math.pow(a, 0.8);
  const z = zcr[i];
  // vocal según brillo: bajo -> ou/oh, medio -> aa, alto -> ee/ih (fricativas: boca casi cerrada)
  let v = z < 0.035 ? 'ou' : z < 0.06 ? 'oh' : z < 0.10 ? 'aa' : z < 0.16 ? 'ee' : 'ih';
  if (z > 0.25) a *= 0.35;
  return { a: +a.toFixed(3), v };
});
// suavizado (ataque rápido, caída lenta) para que no tiemble
for (let i = 1; i < frames.length; i++) { const p = frames[i - 1].a; if (frames[i].a < p) frames[i].a = +(p * 0.55 + frames[i].a * 0.45).toFixed(3); }
process.stdout.write(JSON.stringify({ fps: Number(fps), frames }));
