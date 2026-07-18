function nextPractice(state,today){if(state.lastPractice===today)return state;return{...state,lastPractice:today,streak:state.streak+1,merit:state.merit+10}}
function readingProgress(done,total){return total?Math.round(done/total*100):0}
function safeAiMessage(error){return error?'连接暂时不可用，请稍后重试；你仍可离线研读经典。':'回答成功'}
module.exports={nextPractice,readingProgress,safeAiMessage}
