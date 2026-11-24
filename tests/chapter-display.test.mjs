import test from 'node:test';import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';
const app=await readFile(new URL('../app.js',import.meta.url),'utf8');
test('Kapitelanzeige berechnet Aufgabenanzahl aus den Daten',()=>{
 assert.match(app,/chapterTasks\(ch\.id\)\.length/);
 assert.doesNotMatch(app,/8 Aufgaben pro Kapitel/);
});
test('Symbol-Drops, Diagrammabgabe und Legende sind integriert',()=>{
 assert.match(app,/data-symbol-drop/);assert.match(app,/data-slot-answer/);assert.match(app,/data-upload/);assert.match(app,/renderLegend/);
});
