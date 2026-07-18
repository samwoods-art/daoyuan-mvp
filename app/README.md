# 道缘 App

Expo / React Native 跨平台 MVP。现有仓库根目录 PWA 保持不变；本目录是可维护的正式 App。

## 功能
- 首页每日上香打卡、连续天数与习惯积分（本地持久化）
- 合规“每日一签”自我反思体验
- 《太乙金华宗旨》五章研读与进度
- 真符文化图册占位（待替换真实素材）
- 问道助手成功/失败示例状态（生产环境应走服务端RAG代理）
- iOS、Android、Web

## 运行
```bash
npm install
npm start
# 或 npm run web / npm run ios / npm run android
npm run typecheck
npm test
```

复制 `.env.example` 为 `.env` 并配置Supabase。Gemini密钥不得放在`EXPO_PUBLIC_*`客户端变量；应由Supabase Edge Function保管并实施限流、鉴权和知识库检索。

## 待接真实资源
Supabase项目、服务端AI代理、六张真符原图、道长资料、完整经典版权内容、App Store/Google Play开发者账号和隐私政策主体信息。
