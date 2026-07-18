const test=require('node:test'),assert=require('node:assert/strict');const {nextPractice,readingProgress,safeAiMessage}=require('../src/domain')
test('daily practice increments once',()=>{let s={streak:3,merit:120};s=nextPractice(s,'2026-07-18');assert.equal(s.streak,4);assert.deepEqual(nextPractice(s,'2026-07-18'),s)})
test('reading progress',()=>assert.equal(readingProgress(3,5),60))
test('AI failure is safe and useful',()=>assert.match(safeAiMessage(true),/离线研读/))
