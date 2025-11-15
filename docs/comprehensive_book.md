# React Email - Comprehensive Documentation Book

**Repository:** react-email
**Generated:** 2025-11-15T20:39:36.371179Z

---

## Table of Contents

This book is organized by folder, with each folder's documentation presented as a chapter.

1. [Root](#root)
2. [apps](#apps)
3. [apps/demo](#apps-demo)
4. [apps/demo/emails](#apps-demo-emails)
5. [apps/demo/emails/magic-links](#apps-demo-emails-magic-links)
6. [apps/demo/emails/newsletters](#apps-demo-emails-newsletters)
7. [apps/demo/emails/notifications](#apps-demo-emails-notifications)
8. [apps/demo/emails/receipts](#apps-demo-emails-receipts)
9. [apps/demo/emails/reset-password](#apps-demo-emails-reset-password)
10. [apps/demo/emails/reviews](#apps-demo-emails-reviews)
11. [apps/demo/emails/static](#apps-demo-emails-static)
12. [apps/demo/emails/welcome](#apps-demo-emails-welcome)
13. [apps/docs](#apps-docs)
14. [apps/docs/components](#apps-docs-components)
15. [apps/docs/contributing](#apps-docs-contributing)
16. [apps/docs/contributing/development-workflow](#apps-docs-contributing-development-workflow)
17. [apps/docs/getting-started](#apps-docs-getting-started)
18. [apps/docs/getting-started/monorepo-setup](#apps-docs-getting-started-monorepo-setup)
19. [apps/docs/images](#apps-docs-images)
20. [apps/docs/integrations](#apps-docs-integrations)
21. [apps/docs/logo](#apps-docs-logo)
22. [apps/docs/snippets](#apps-docs-snippets)
23. [apps/docs/utilities](#apps-docs-utilities)
24. [apps/web](#apps-web)
25. [apps/web/components](#apps-web-components)
26. [apps/web/components/_components](#apps-web-components-_components)
27. [apps/web/components/article-with-image](#apps-web-components-article-with-image)
28. [apps/web/components/article-with-image-as-background](#apps-web-components-article-with-image-as-background)
29. [apps/web/components/article-with-image-on-right](#apps-web-components-article-with-image-on-right)
30. [apps/web/components/article-with-multiple-authors](#apps-web-components-article-with-multiple-authors)
31. [apps/web/components/article-with-single-author](#apps-web-components-article-with-single-author)
32. [apps/web/components/article-with-two-cards](#apps-web-components-article-with-two-cards)
33. [apps/web/components/avatars-circular](#apps-web-components-avatars-circular)
34. [apps/web/components/avatars-group-stacked](#apps-web-components-avatars-group-stacked)
35. [apps/web/components/avatars-rounded](#apps-web-components-avatars-rounded)
36. [apps/web/components/avatars-with-text](#apps-web-components-avatars-with-text)
37. [apps/web/components/bento-grid](#apps-web-components-bento-grid)
38. [apps/web/components/checkout](#apps-web-components-checkout)
39. [apps/web/components/code-block-with-custom-theme](#apps-web-components-code-block-with-custom-theme)
40. [apps/web/components/code-block-with-line-numbers](#apps-web-components-code-block-with-line-numbers)
41. [apps/web/components/code-block-with-predefined-theme](#apps-web-components-code-block-with-predefined-theme)
42. [apps/web/components/code-block-without-theme](#apps-web-components-code-block-without-theme)
43. [apps/web/components/code-inline-with-different-colors](#apps-web-components-code-inline-with-different-colors)
44. [apps/web/components/customer-reviews](#apps-web-components-customer-reviews)
45. [apps/web/components/divider-between-rows-and-columns](#apps-web-components-divider-between-rows-and-columns)
46. [apps/web/components/download-buttons](#apps-web-components-download-buttons)
47. [apps/web/components/footer-with-one-column](#apps-web-components-footer-with-one-column)
48. [apps/web/components/footer-with-two-columns](#apps-web-components-footer-with-two-columns)
49. [apps/web/components/four-images-in-a-grid](#apps-web-components-four-images-in-a-grid)
50. [apps/web/components/header-and-four-paragraphs](#apps-web-components-header-and-four-paragraphs)
51. [apps/web/components/header-and-four-paragraphs-and-two-columns](#apps-web-components-header-and-four-paragraphs-and-two-columns)
52. [apps/web/components/header-and-list-items](#apps-web-components-header-and-list-items)
53. [apps/web/components/header-and-numbered-list-items](#apps-web-components-header-and-numbered-list-items)
54. [apps/web/components/header-and-three-centered-paragraphs](#apps-web-components-header-and-three-centered-paragraphs)
55. [apps/web/components/header-with-centered-menu](#apps-web-components-header-with-centered-menu)
56. [apps/web/components/header-with-side-menu](#apps-web-components-header-with-side-menu)
57. [apps/web/components/header-with-social-icons](#apps-web-components-header-with-social-icons)
58. [apps/web/components/image-with-varying-sizes](#apps-web-components-image-with-varying-sizes)
59. [apps/web/components/images-on-horizontal-grid](#apps-web-components-images-on-horizontal-grid)
60. [apps/web/components/images-on-vertical-grid](#apps-web-components-images-on-vertical-grid)
61. [apps/web/components/link-inline-with-text](#apps-web-components-link-inline-with-text)
62. [apps/web/components/list-with-image-on-left](#apps-web-components-list-with-image-on-left)
63. [apps/web/components/markdown-with-container-styles](#apps-web-components-markdown-with-container-styles)
64. [apps/web/components/markdown-with-custom-styles](#apps-web-components-markdown-with-custom-styles)
65. [apps/web/components/multiple-headings](#apps-web-components-multiple-headings)
66. [apps/web/components/one-product](#apps-web-components-one-product)
67. [apps/web/components/one-product-with-image-on-the-left](#apps-web-components-one-product-with-image-on-the-left)
68. [apps/web/components/one-row-three-columns](#apps-web-components-one-row-three-columns)
69. [apps/web/components/one-row-two-columns](#apps-web-components-one-row-two-columns)
70. [apps/web/components/rounded-image](#apps-web-components-rounded-image)
71. [apps/web/components/section-with-rows-and-columns](#apps-web-components-section-with-rows-and-columns)
72. [apps/web/components/simple-code-inline](#apps-web-components-simple-code-inline)
73. [apps/web/components/simple-container](#apps-web-components-simple-container)
74. [apps/web/components/simple-divider](#apps-web-components-simple-divider)
75. [apps/web/components/simple-heading](#apps-web-components-simple-heading)
76. [apps/web/components/simple-image](#apps-web-components-simple-image)
77. [apps/web/components/simple-link](#apps-web-components-simple-link)
78. [apps/web/components/simple-list](#apps-web-components-simple-list)
79. [apps/web/components/simple-markdown](#apps-web-components-simple-markdown)
80. [apps/web/components/simple-pricing-table](#apps-web-components-simple-pricing-table)
81. [apps/web/components/simple-rating-survey](#apps-web-components-simple-rating-survey)
82. [apps/web/components/simple-section](#apps-web-components-simple-section)
83. [apps/web/components/simple-text](#apps-web-components-simple-text)
84. [apps/web/components/single-button](#apps-web-components-single-button)
85. [apps/web/components/static](#apps-web-components-static)
86. [apps/web/components/stats-simple](#apps-web-components-stats-simple)
87. [apps/web/components/stats-stepped](#apps-web-components-stats-stepped)
88. [apps/web/components/survey-section](#apps-web-components-survey-section)
89. [apps/web/components/testimonial-simple-centered](#apps-web-components-testimonial-simple-centered)
90. [apps/web/components/testimonial-with-large-avatar](#apps-web-components-testimonial-with-large-avatar)
91. [apps/web/components/text-with-styling](#apps-web-components-text-with-styling)
92. [apps/web/components/three-columns-with-images](#apps-web-components-three-columns-with-images)
93. [apps/web/components/title-four-cards](#apps-web-components-title-four-cards)
94. [apps/web/components/title-three-cards-in-a-row](#apps-web-components-title-three-cards-in-a-row)
95. [apps/web/components/two-buttons](#apps-web-components-two-buttons)
96. [apps/web/components/two-tiers-with-emphasized-tier](#apps-web-components-two-tiers-with-emphasized-tier)
97. [apps/web/public](#apps-web-public)
98. [apps/web/public/brand](#apps-web-public-brand)
99. [apps/web/public/examples](#apps-web-public-examples)
100. [apps/web/public/examples/authors](#apps-web-public-examples-authors)
101. [apps/web/public/fonts](#apps-web-public-fonts)
102. [apps/web/public/fonts/commit-mono](#apps-web-public-fonts-commit-mono)
103. [apps/web/public/fonts/inter](#apps-web-public-fonts-inter)
104. [apps/web/public/fonts/shantell-sans](#apps-web-public-fonts-shantell-sans)
105. [apps/web/public/js](#apps-web-public-js)
106. [apps/web/public/meta](#apps-web-public-meta)
107. [apps/web/public/static](#apps-web-public-static)
108. [apps/web/public/static/components](#apps-web-public-static-components)
109. [apps/web/public/static/covers](#apps-web-public-static-covers)
110. [apps/web/public/static/icons](#apps-web-public-static-icons)
111. [apps/web/src](#apps-web-src)
112. [apps/web/src/app](#apps-web-src-app)
113. [apps/web/src/app/api](#apps-web-src-app-api)
114. [apps/web/src/app/api/check-spam](#apps-web-src-app-api-check-spam)
115. [apps/web/src/app/api/check-spam/__snapshots__](#apps-web-src-app-api-check-spam-__snapshots__)
116. [apps/web/src/app/api/check-spam/testing](#apps-web-src-app-api-check-spam-testing)
117. [apps/web/src/app/api/send](#apps-web-src-app-api-send)
118. [apps/web/src/app/api/send/test](#apps-web-src-app-api-send-test)
119. [apps/web/src/app/components](#apps-web-src-app-components)
120. [apps/web/src/app/components/[slug]](#apps-web-src-app-components-[slug])
121. [apps/web/src/app/templates](#apps-web-src-app-templates)
122. [apps/web/src/components](#apps-web-src-components)
123. [apps/web/src/components/icons](#apps-web-src-components-icons)
124. [apps/web/src/components/sections](#apps-web-src-components-sections)
125. [apps/web/src/components/sections/playground](#apps-web-src-components-sections-playground)
126. [apps/web/src/components/sections/tools](#apps-web-src-components-sections-tools)
127. [apps/web/src/hooks](#apps-web-src-hooks)
128. [apps/web/src/illustrations](#apps-web-src-illustrations)
129. [apps/web/src/styles](#apps-web-src-styles)
130. [apps/web/src/types](#apps-web-src-types)
131. [apps/web/src/utils](#apps-web-src-utils)
132. [apps/web/src/utils/spam-assassin](#apps-web-src-utils-spam-assassin)
133. [apps/web/src/utils/spam-assassin/__snapshots__](#apps-web-src-utils-spam-assassin-__snapshots__)
134. [apps/web/src/webgl](#apps-web-src-webgl)
135. [apps/web/src/webgl/materials](#apps-web-src-webgl-materials)
136. [benchmarks](#benchmarks)
137. [benchmarks/preview-server](#benchmarks-preview-server)
138. [benchmarks/preview-server/src](#benchmarks-preview-server-src)
139. [benchmarks/preview-server/src/utils](#benchmarks-preview-server-src-utils)
140. [benchmarks/tailwind-component](#benchmarks-tailwind-component)
141. [benchmarks/tailwind-component/src](#benchmarks-tailwind-component-src)
142. [benchmarks/tailwind-component/src/emails](#benchmarks-tailwind-component-src-emails)
143. [examples](#examples)
144. [examples/aws-ses](#examples-aws-ses)
145. [examples/aws-ses/src](#examples-aws-ses-src)
146. [examples/mailersend](#examples-mailersend)
147. [examples/mailersend/src](#examples-mailersend-src)
148. [examples/nodemailer](#examples-nodemailer)
149. [examples/nodemailer/src](#examples-nodemailer-src)
150. [examples/plunk](#examples-plunk)
151. [examples/plunk/src](#examples-plunk-src)
152. [examples/postmark](#examples-postmark)
153. [examples/postmark/src](#examples-postmark-src)
154. [examples/resend](#examples-resend)
155. [examples/resend/src](#examples-resend-src)
156. [examples/resend/src/lib](#examples-resend-src-lib)
157. [examples/resend/src/pages](#examples-resend-src-pages)
158. [examples/resend/src/pages/api](#examples-resend-src-pages-api)
159. [examples/resend/transactional](#examples-resend-transactional)
160. [examples/resend/transactional/emails](#examples-resend-transactional-emails)
161. [examples/scaleway](#examples-scaleway)
162. [examples/scaleway/next](#examples-scaleway-next)
163. [examples/scaleway/next/src](#examples-scaleway-next-src)
164. [examples/scaleway/next/src/lib](#examples-scaleway-next-src-lib)
165. [examples/scaleway/next/src/pages](#examples-scaleway-next-src-pages)
166. [examples/scaleway/next/src/pages/api](#examples-scaleway-next-src-pages-api)
167. [examples/scaleway/next/transactional](#examples-scaleway-next-transactional)
168. [examples/scaleway/next/transactional/emails](#examples-scaleway-next-transactional-emails)
169. [examples/scaleway/node](#examples-scaleway-node)
170. [examples/scaleway/node/src](#examples-scaleway-node-src)
171. [examples/sendgrid](#examples-sendgrid)
172. [examples/sendgrid/src](#examples-sendgrid-src)
173. [packages](#packages)
174. [packages/body](#packages-body)
175. [packages/body/src](#packages-body-src)
176. [packages/body/src/__snapshots__](#packages-body-src-__snapshots__)
177. [packages/button](#packages-button)
178. [packages/button/src](#packages-button-src)
179. [packages/button/src/__snapshots__](#packages-button-src-__snapshots__)
180. [packages/button/src/utils](#packages-button-src-utils)
181. [packages/code-block](#packages-code-block)
182. [packages/code-block/src](#packages-code-block-src)
183. [packages/code-inline](#packages-code-inline)
184. [packages/code-inline/src](#packages-code-inline-src)
185. [packages/column](#packages-column)
186. [packages/column/src](#packages-column-src)
187. [packages/column/src/__snapshots__](#packages-column-src-__snapshots__)
188. [packages/components](#packages-components)
189. [packages/components/src](#packages-components-src)
190. [packages/components/src/__snapshots__](#packages-components-src-__snapshots__)
191. [packages/container](#packages-container)
192. [packages/container/src](#packages-container-src)
193. [packages/container/src/__snapshots__](#packages-container-src-__snapshots__)
194. [packages/create-email](#packages-create-email)
195. [packages/create-email/src](#packages-create-email-src)
196. [packages/create-email/template](#packages-create-email-template)
197. [packages/create-email/template/emails](#packages-create-email-template-emails)
198. [packages/create-email/template/emails/static](#packages-create-email-template-emails-static)
199. [packages/font](#packages-font)
200. [packages/font/src](#packages-font-src)
201. [packages/font/src/__snapshots__](#packages-font-src-__snapshots__)
202. [packages/head](#packages-head)
203. [packages/head/src](#packages-head-src)
204. [packages/head/src/__snapshots__](#packages-head-src-__snapshots__)
205. [packages/heading](#packages-heading)
206. [packages/heading/src](#packages-heading-src)
207. [packages/heading/src/__snapshots__](#packages-heading-src-__snapshots__)
208. [packages/heading/src/utils](#packages-heading-src-utils)
209. [packages/hr](#packages-hr)
210. [packages/hr/src](#packages-hr-src)
211. [packages/hr/src/__snapshots__](#packages-hr-src-__snapshots__)
212. [packages/html](#packages-html)
213. [packages/html/src](#packages-html-src)
214. [packages/html/src/__snapshots__](#packages-html-src-__snapshots__)
215. [packages/img](#packages-img)
216. [packages/img/src](#packages-img-src)
217. [packages/img/src/__snapshots__](#packages-img-src-__snapshots__)
218. [packages/link](#packages-link)
219. [packages/link/src](#packages-link-src)
220. [packages/link/src/__snapshots__](#packages-link-src-__snapshots__)
221. [packages/markdown](#packages-markdown)
222. [packages/markdown/src](#packages-markdown-src)
223. [packages/markdown/src/__snapshots__](#packages-markdown-src-__snapshots__)
224. [packages/markdown/src/utils](#packages-markdown-src-utils)
225. [packages/preview](#packages-preview)
226. [packages/preview-server](#packages-preview-server)
227. [packages/preview-server/emails](#packages-preview-server-emails)
228. [packages/preview-server/jsx-runtime](#packages-preview-server-jsx-runtime)
229. [packages/preview-server/scripts](#packages-preview-server-scripts)
230. [packages/preview-server/scripts/utils](#packages-preview-server-scripts-utils)
231. [packages/preview-server/scripts/utils/default-seed](#packages-preview-server-scripts-utils-default-seed)
232. [packages/preview-server/scripts/utils/default-seed/auth](#packages-preview-server-scripts-utils-default-seed-auth)
233. [packages/preview-server/scripts/utils/default-seed/communications](#packages-preview-server-scripts-utils-default-seed-communications)
234. [packages/preview-server/scripts/utils/default-seed/marketing](#packages-preview-server-scripts-utils-default-seed-marketing)
235. [packages/preview-server/src](#packages-preview-server-src)
236. [packages/preview-server/src/actions](#packages-preview-server-src-actions)
237. [packages/preview-server/src/actions/email-validation](#packages-preview-server-src-actions-email-validation)
238. [packages/preview-server/src/actions/email-validation/__snapshots__](#packages-preview-server-src-actions-email-validation-__snapshots__)
239. [packages/preview-server/src/animated-icons-data](#packages-preview-server-src-animated-icons-data)
240. [packages/preview-server/src/app](#packages-preview-server-src-app)
241. [packages/preview-server/src/app/fonts](#packages-preview-server-src-app-fonts)
242. [packages/preview-server/src/app/fonts/SFMono](#packages-preview-server-src-app-fonts-sfmono)
243. [packages/preview-server/src/app/preview](#packages-preview-server-src-app-preview)
244. [packages/preview-server/src/app/preview/[...slug]](#packages-preview-server-src-app-preview-[...slug])
245. [packages/preview-server/src/components](#packages-preview-server-src-components)
246. [packages/preview-server/src/components/icons](#packages-preview-server-src-components-icons)
247. [packages/preview-server/src/components/sidebar](#packages-preview-server-src-components-sidebar)
248. [packages/preview-server/src/components/toolbar](#packages-preview-server-src-components-toolbar)
249. [packages/preview-server/src/components/topbar](#packages-preview-server-src-components-topbar)
250. [packages/preview-server/src/contexts](#packages-preview-server-src-contexts)
251. [packages/preview-server/src/hooks](#packages-preview-server-src-hooks)
252. [packages/preview-server/src/utils](#packages-preview-server-src-utils)
253. [packages/preview-server/src/utils/__snapshots__](#packages-preview-server-src-utils-__snapshots__)
254. [packages/preview-server/src/utils/caniemail](#packages-preview-server-src-utils-caniemail)
255. [packages/preview-server/src/utils/caniemail/ast](#packages-preview-server-src-utils-caniemail-ast)
256. [packages/preview-server/src/utils/caniemail/ast/__snapshots__](#packages-preview-server-src-utils-caniemail-ast-__snapshots__)
257. [packages/preview-server/src/utils/caniemail/tailwind](#packages-preview-server-src-utils-caniemail-tailwind)
258. [packages/preview-server/src/utils/caniemail/tailwind/tests](#packages-preview-server-src-utils-caniemail-tailwind-tests)
259. [packages/preview-server/src/utils/esbuild](#packages-preview-server-src-utils-esbuild)
260. [packages/preview-server/src/utils/testing](#packages-preview-server-src-utils-testing)
261. [packages/preview-server/src/utils/types](#packages-preview-server-src-utils-types)
262. [packages/preview/src](#packages-preview-src)
263. [packages/preview/src/__snapshots__](#packages-preview-src-__snapshots__)
264. [packages/react-email](#packages-react-email)
265. [packages/react-email/dev](#packages-react-email-dev)
266. [packages/react-email/src](#packages-react-email-src)
267. [packages/react-email/src/actions](#packages-react-email-src-actions)
268. [packages/react-email/src/actions/email-validation](#packages-react-email-src-actions-email-validation)
269. [packages/react-email/src/actions/email-validation/__snapshots__](#packages-react-email-src-actions-email-validation-__snapshots__)
270. [packages/react-email/src/cli](#packages-react-email-src-cli)
271. [packages/react-email/src/cli/utils](#packages-react-email-src-cli-utils)
272. [packages/react-email/src/cli/utils/preview](#packages-react-email-src-cli-utils-preview)
273. [packages/react-email/src/cli/utils/preview/hot-reloading](#packages-react-email-src-cli-utils-preview-hot-reloading)
274. [packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__](#packages-react-email-src-cli-utils-preview-hot-reloading-__snapshots__)
275. [packages/react-email/src/cli/utils/preview/hot-reloading/test](#packages-react-email-src-cli-utils-preview-hot-reloading-test)
276. [packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph](#packages-react-email-src-cli-utils-preview-hot-reloading-test-dependency-graph)
277. [packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner](#packages-react-email-src-cli-utils-preview-hot-reloading-test-dependency-graph-inner)
278. [packages/react-email/src/commands](#packages-react-email-src-commands)
279. [packages/react-email/src/commands/resend](#packages-react-email-src-commands-resend)
280. [packages/react-email/src/commands/testing](#packages-react-email-src-commands-testing)
281. [packages/react-email/src/commands/testing/__snapshots__](#packages-react-email-src-commands-testing-__snapshots__)
282. [packages/react-email/src/commands/testing/emails](#packages-react-email-src-commands-testing-emails)
283. [packages/react-email/src/utils](#packages-react-email-src-utils)
284. [packages/react-email/src/utils/__snapshots__](#packages-react-email-src-utils-__snapshots__)
285. [packages/react-email/src/utils/esbuild](#packages-react-email-src-utils-esbuild)
286. [packages/react-email/src/utils/preview](#packages-react-email-src-utils-preview)
287. [packages/react-email/src/utils/preview/hot-reloading](#packages-react-email-src-utils-preview-hot-reloading)
288. [packages/react-email/src/utils/preview/hot-reloading/__snapshots__](#packages-react-email-src-utils-preview-hot-reloading-__snapshots__)
289. [packages/react-email/src/utils/preview/hot-reloading/test](#packages-react-email-src-utils-preview-hot-reloading-test)
290. [packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph](#packages-react-email-src-utils-preview-hot-reloading-test-dependency-graph)
291. [packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph/inner](#packages-react-email-src-utils-preview-hot-reloading-test-dependency-graph-inner)
292. [packages/react-email/src/utils/types](#packages-react-email-src-utils-types)
293. [packages/render](#packages-render)
294. [packages/render/src](#packages-render-src)
295. [packages/render/src/browser](#packages-render-src-browser)
296. [packages/render/src/browser/__snapshots__](#packages-render-src-browser-__snapshots__)
297. [packages/render/src/edge](#packages-render-src-edge)
298. [packages/render/src/edge/__snapshots__](#packages-render-src-edge-__snapshots__)
299. [packages/render/src/node](#packages-render-src-node)
300. [packages/render/src/node/__snapshots__](#packages-render-src-node-__snapshots__)
301. [packages/render/src/shared](#packages-render-src-shared)
302. [packages/render/src/shared/utils](#packages-render-src-shared-utils)
303. [packages/render/src/shared/utils/__snapshots__](#packages-render-src-shared-utils-__snapshots__)
304. [packages/render/src/shared/utils/testing](#packages-render-src-shared-utils-testing)
305. [packages/row](#packages-row)
306. [packages/row/src](#packages-row-src)
307. [packages/row/src/__snapshots__](#packages-row-src-__snapshots__)
308. [packages/section](#packages-section)
309. [packages/section/src](#packages-section-src)
310. [packages/section/src/__snapshots__](#packages-section-src-__snapshots__)
311. [packages/tailwind](#packages-tailwind)
312. [packages/tailwind/integrations](#packages-tailwind-integrations)
313. [packages/tailwind/integrations/nextjs](#packages-tailwind-integrations-nextjs)
314. [packages/tailwind/integrations/nextjs/emails](#packages-tailwind-integrations-nextjs-emails)
315. [packages/tailwind/integrations/nextjs/src](#packages-tailwind-integrations-nextjs-src)
316. [packages/tailwind/integrations/nextjs/src/app](#packages-tailwind-integrations-nextjs-src-app)
317. [packages/tailwind/integrations/vite](#packages-tailwind-integrations-vite)
318. [packages/tailwind/integrations/vite/emails](#packages-tailwind-integrations-vite-emails)
319. [packages/tailwind/integrations/vite/public](#packages-tailwind-integrations-vite-public)
320. [packages/tailwind/integrations/vite/src](#packages-tailwind-integrations-vite-src)
321. [packages/tailwind/src](#packages-tailwind-src)
322. [packages/tailwind/src/__snapshots__](#packages-tailwind-src-__snapshots__)
323. [packages/tailwind/src/hooks](#packages-tailwind-src-hooks)
324. [packages/tailwind/src/utils](#packages-tailwind-src-utils)
325. [packages/tailwind/src/utils/__snapshots__](#packages-tailwind-src-utils-__snapshots__)
326. [packages/tailwind/src/utils/compatibility](#packages-tailwind-src-utils-compatibility)
327. [packages/tailwind/src/utils/css](#packages-tailwind-src-utils-css)
328. [packages/tailwind/src/utils/css/__snapshots__](#packages-tailwind-src-utils-css-__snapshots__)
329. [packages/tailwind/src/utils/react](#packages-tailwind-src-utils-react)
330. [packages/tailwind/src/utils/tailwindcss](#packages-tailwind-src-utils-tailwindcss)
331. [packages/tailwind/src/utils/tailwindcss/__snapshots__](#packages-tailwind-src-utils-tailwindcss-__snapshots__)
332. [packages/tailwind/src/utils/tailwindcss/tailwind-stylesheets](#packages-tailwind-src-utils-tailwindcss-tailwind-stylesheets)
333. [packages/tailwind/src/utils/text](#packages-tailwind-src-utils-text)
334. [packages/text](#packages-text)
335. [packages/text/src](#packages-text-src)
336. [packages/text/src/__snapshots__](#packages-text-src-__snapshots__)
337. [packages/text/src/utils](#packages-text-src-utils)
338. [packages/tsconfig](#packages-tsconfig)
339. [playground](#playground)
340. [playground/emails](#playground-emails)
341. [scripts](#scripts)

---

# Chapter 1: Root


**Folder Path:** `/`
**Generated:** 2025-11-15T20:38:37.368434Z

---

## Overview

This is the root directory of the react-email repository. React Email is a library for building email templates with React components.

## Structure

- **Subdirectories:** 6
- **Documentation Files:** 15
- **Keyword Files:** 15

### Subdirectories

- `apps/`
- `benchmarks/`
- `examples/`
- `packages/`
- `playground/`
- `scripts/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in Root



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `.npmrc` | [View](.npmrc_docs.md) | [View](.npmrc_kw.md) |
| `CONTRIBUTING.md` | [View](CONTRIBUTING.md_docs.md) | [View](CONTRIBUTING.md_kw.md) |
| `LICENSE.md` | [View](LICENSE.md_docs.md) | [View](LICENSE.md_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `SECURITY.md` | [View](SECURITY.md_docs.md) | [View](SECURITY.md_kw.md) |
| `biome.json` | [View](biome.json_docs.md) | [View](biome.json_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `pnpm-lock.yaml` | [View](pnpm-lock.yaml_docs.md) | [View](pnpm-lock.yaml_kw.md) |
| `pnpm-workspace.yaml` | [View](pnpm-workspace.yaml_docs.md) | [View](pnpm-workspace.yaml_kw.md) |
| `renovate.json` | [View](renovate.json_docs.md) | [View](renovate.json_kw.md) |
| `scan_repo.py` | [View](scan_repo.py_docs.md) | [View](scan_repo.py_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `turbo.json` | [View](turbo.json_docs.md) | [View](turbo.json_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](index.md)

---

# Chapter 2: apps


**Folder Path:** `apps`
**Generated:** 2025-11-15T20:38:37.393762Z

---

## Overview

This directory (`apps`) contains 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `demo/`
- `docs/`
- `web/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps

---

# Chapter 3: apps/demo


**Folder Path:** `apps/demo`
**Generated:** 2025-11-15T20:38:37.395040Z

---

## Overview

This directory (`apps/demo`) contains a Node.js package. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 4: apps/demo/emails


**Folder Path:** `apps/demo/emails`
**Generated:** 2025-11-15T20:38:37.396458Z

---

## Overview

This directory (`apps/demo/emails`) contains 

## Structure

- **Subdirectories:** 8
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `magic-links/`
- `newsletters/`
- `notifications/`
- `receipts/`
- `reset-password/`
- `reviews/`
- `static/`
- `welcome/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `tailwind.config.ts` | [View](tailwind.config.ts_docs.md) | [View](tailwind.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 5: apps/demo/emails/magic-links


**Folder Path:** `apps/demo/emails/magic-links`
**Generated:** 2025-11-15T20:38:37.397571Z

---

## Overview

This directory (`apps/demo/emails/magic-links`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 6
- **Keyword Files:** 6

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/magic-links



| File | Documentation | Keywords |
|------|---------------|----------|
| `aws-verify-email.tsx` | [View](aws-verify-email.tsx_docs.md) | [View](aws-verify-email.tsx_kw.md) |
| `linear-login-code.tsx` | [View](linear-login-code.tsx_docs.md) | [View](linear-login-code.tsx_kw.md) |
| `notion-magic-link.tsx` | [View](notion-magic-link.tsx_docs.md) | [View](notion-magic-link.tsx_kw.md) |
| `plaid-verify-identity.tsx` | [View](plaid-verify-identity.tsx_docs.md) | [View](plaid-verify-identity.tsx_kw.md) |
| `raycast-magic-link.tsx` | [View](raycast-magic-link.tsx_docs.md) | [View](raycast-magic-link.tsx_kw.md) |
| `slack-confirm.tsx` | [View](slack-confirm.tsx_docs.md) | [View](slack-confirm.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 6: apps/demo/emails/newsletters


**Folder Path:** `apps/demo/emails/newsletters`
**Generated:** 2025-11-15T20:38:37.400670Z

---

## Overview

This directory (`apps/demo/emails/newsletters`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/newsletters



| File | Documentation | Keywords |
|------|---------------|----------|
| `codepen-challengers.tsx` | [View](codepen-challengers.tsx_docs.md) | [View](codepen-challengers.tsx_kw.md) |
| `google-play-policy-update.tsx` | [View](google-play-policy-update.tsx_docs.md) | [View](google-play-policy-update.tsx_kw.md) |
| `stack-overflow-tips.tsx` | [View](stack-overflow-tips.tsx_docs.md) | [View](stack-overflow-tips.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 7: apps/demo/emails/notifications


**Folder Path:** `apps/demo/emails/notifications`
**Generated:** 2025-11-15T20:38:37.403353Z

---

## Overview

This directory (`apps/demo/emails/notifications`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/notifications



| File | Documentation | Keywords |
|------|---------------|----------|
| `github-access-token.tsx` | [View](github-access-token.tsx_docs.md) | [View](github-access-token.tsx_kw.md) |
| `papermark-year-in-review.tsx` | [View](papermark-year-in-review.tsx_docs.md) | [View](papermark-year-in-review.tsx_kw.md) |
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |
| `yelp-recent-login.tsx` | [View](yelp-recent-login.tsx_docs.md) | [View](yelp-recent-login.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 8: apps/demo/emails/receipts


**Folder Path:** `apps/demo/emails/receipts`
**Generated:** 2025-11-15T20:38:37.406272Z

---

## Overview

This directory (`apps/demo/emails/receipts`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/receipts



| File | Documentation | Keywords |
|------|---------------|----------|
| `apple-receipt.tsx` | [View](apple-receipt.tsx_docs.md) | [View](apple-receipt.tsx_kw.md) |
| `nike-receipt.tsx` | [View](nike-receipt.tsx_docs.md) | [View](nike-receipt.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 9: apps/demo/emails/reset-password


**Folder Path:** `apps/demo/emails/reset-password`
**Generated:** 2025-11-15T20:38:37.408590Z

---

## Overview

This directory (`apps/demo/emails/reset-password`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/reset-password



| File | Documentation | Keywords |
|------|---------------|----------|
| `dropbox-reset-password.tsx` | [View](dropbox-reset-password.tsx_docs.md) | [View](dropbox-reset-password.tsx_kw.md) |
| `twitch-reset-password.tsx` | [View](twitch-reset-password.tsx_docs.md) | [View](twitch-reset-password.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 10: apps/demo/emails/reviews


**Folder Path:** `apps/demo/emails/reviews`
**Generated:** 2025-11-15T20:38:37.410638Z

---

## Overview

This directory (`apps/demo/emails/reviews`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/reviews



| File | Documentation | Keywords |
|------|---------------|----------|
| `airbnb-review.tsx` | [View](airbnb-review.tsx_docs.md) | [View](airbnb-review.tsx_kw.md) |
| `amazon-review.tsx` | [View](amazon-review.tsx_docs.md) | [View](amazon-review.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 11: apps/demo/emails/static


**Folder Path:** `apps/demo/emails/static`
**Generated:** 2025-11-15T20:38:37.412845Z

---

## Overview

This directory (`apps/demo/emails/static`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 59
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/static



| File | Documentation | Keywords |
|------|---------------|----------|
| `airbnb-logo.png` | [View](airbnb-logo.png_docs.md) | - |
| `airbnb-review-user.jpg` | [View](airbnb-review-user.jpg_docs.md) | - |
| `amazon-book.jpg` | [View](amazon-book.jpg_docs.md) | - |
| `amazon-facebook.jpg` | [View](amazon-facebook.jpg_docs.md) | - |
| `amazon-instagram.jpg` | [View](amazon-instagram.jpg_docs.md) | - |
| `amazon-logo.png` | [View](amazon-logo.png_docs.md) | - |
| `amazon-prime-logo.png` | [View](amazon-prime-logo.png_docs.md) | - |
| `amazon-rating.gif` | [View](amazon-rating.gif_docs.md) | - |
| `amazon-twitter.jpg` | [View](amazon-twitter.jpg_docs.md) | - |
| `apple-card-icon.png` | [View](apple-card-icon.png_docs.md) | - |
| `apple-hbo-max-icon.jpeg` | [View](apple-hbo-max-icon.jpeg_docs.md) | - |
| `apple-logo.png` | [View](apple-logo.png_docs.md) | - |
| `apple-wallet.png` | [View](apple-wallet.png_docs.md) | - |
| `aws-logo.png` | [View](aws-logo.png_docs.md) | - |
| `codepen-challengers.png` | [View](codepen-challengers.png_docs.md) | - |
| `codepen-cube.png` | [View](codepen-cube.png_docs.md) | - |
| `codepen-pro.png` | [View](codepen-pro.png_docs.md) | - |
| `dropbox-logo.png` | [View](dropbox-logo.png_docs.md) | - |
| `github.png` | [View](github.png_docs.md) | - |
| `google-play-academy.png` | [View](google-play-academy.png_docs.md) | - |
| `google-play-chat.png` | [View](google-play-chat.png_docs.md) | - |
| `google-play-footer.png` | [View](google-play-footer.png_docs.md) | - |
| `google-play-header.png` | [View](google-play-header.png_docs.md) | - |
| `google-play-icon.png` | [View](google-play-icon.png_docs.md) | - |
| `google-play-logo.png` | [View](google-play-logo.png_docs.md) | - |
| `google-play-pl.png` | [View](google-play-pl.png_docs.md) | - |
| `google-play.png` | [View](google-play.png_docs.md) | - |
| `koala-logo.png` | [View](koala-logo.png_docs.md) | - |
| `linear-logo.png` | [View](linear-logo.png_docs.md) | - |
| `netlify-logo.png` | [View](netlify-logo.png_docs.md) | - |
| `nike-logo.png` | [View](nike-logo.png_docs.md) | - |
| `nike-phone.png` | [View](nike-phone.png_docs.md) | - |
| `nike-product.png` | [View](nike-product.png_docs.md) | - |
| `nike-recomendation-1.png` | [View](nike-recomendation-1.png_docs.md) | - |
| `nike-recomendation-2.png` | [View](nike-recomendation-2.png_docs.md) | - |
| `nike-recomendation-3.png` | [View](nike-recomendation-3.png_docs.md) | - |
| `nike-recomendation-4.png` | [View](nike-recomendation-4.png_docs.md) | - |
| `notion-logo.png` | [View](notion-logo.png_docs.md) | - |
| `plaid-logo.png` | [View](plaid-logo.png_docs.md) | - |
| `raycast-bg.png` | [View](raycast-bg.png_docs.md) | - |
| `raycast-logo.png` | [View](raycast-logo.png_docs.md) | - |
| `slack-facebook.png` | [View](slack-facebook.png_docs.md) | - |
| `slack-linkedin.png` | [View](slack-linkedin.png_docs.md) | - |
| `slack-logo.png` | [View](slack-logo.png_docs.md) | - |
| `slack-twitter.png` | [View](slack-twitter.png_docs.md) | - |
| `stack-overflow-header.png` | [View](stack-overflow-header.png_docs.md) | - |
| `stack-overflow-logo-sm.png` | [View](stack-overflow-logo-sm.png_docs.md) | - |
| `stack-overflow-logo.png` | [View](stack-overflow-logo.png_docs.md) | - |
| `stripe-logo.png` | [View](stripe-logo.png_docs.md) | - |
| `twitch-icon-facebook.png` | [View](twitch-icon-facebook.png_docs.md) | - |
| `twitch-icon-twitter.png` | [View](twitch-icon-twitter.png_docs.md) | - |
| `twitch-logo.png` | [View](twitch-logo.png_docs.md) | - |
| `vercel-arrow.png` | [View](vercel-arrow.png_docs.md) | - |
| `vercel-logo.png` | [View](vercel-logo.png_docs.md) | - |
| `vercel-team.png` | [View](vercel-team.png_docs.md) | - |
| `vercel-user.png` | [View](vercel-user.png_docs.md) | - |
| `yelp-footer.png` | [View](yelp-footer.png_docs.md) | - |
| `yelp-header.png` | [View](yelp-header.png_docs.md) | - |
| `yelp-logo.png` | [View](yelp-logo.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 12: apps/demo/emails/welcome


**Folder Path:** `apps/demo/emails/welcome`
**Generated:** 2025-11-15T20:38:37.413612Z

---

## Overview

This directory (`apps/demo/emails/welcome`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/demo/emails/welcome



| File | Documentation | Keywords |
|------|---------------|----------|
| `koala-welcome.tsx` | [View](koala-welcome.tsx_docs.md) | [View](koala-welcome.tsx_kw.md) |
| `netlify-welcome.tsx` | [View](netlify-welcome.tsx_docs.md) | [View](netlify-welcome.tsx_kw.md) |
| `stripe-welcome.tsx` | [View](stripe-welcome.tsx_docs.md) | [View](stripe-welcome.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 13: apps/docs


**Folder Path:** `apps/docs`
**Generated:** 2025-11-15T20:38:37.416164Z

---

## Overview

This directory (`apps/docs`) contains a Node.js package. React components. 

## Structure

- **Subdirectories:** 8
- **Documentation Files:** 10
- **Keyword Files:** 9

### Subdirectories

- `components/`
- `contributing/`
- `getting-started/`
- `images/`
- `integrations/`
- `logo/`
- `snippets/`
- `utilities/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs



| File | Documentation | Keywords |
|------|---------------|----------|
| `changelog.mdx` | [View](changelog.mdx_docs.md) | [View](changelog.mdx_kw.md) |
| `cli.mdx` | [View](cli.mdx_docs.md) | [View](cli.mdx_kw.md) |
| `contributing.mdx` | [View](contributing.mdx_docs.md) | [View](contributing.mdx_kw.md) |
| `deployment.mdx` | [View](deployment.mdx_docs.md) | [View](deployment.mdx_kw.md) |
| `docs.json` | [View](docs.json_docs.md) | [View](docs.json_kw.md) |
| `favicon.png` | [View](favicon.png_docs.md) | - |
| `introduction.mdx` | [View](introduction.mdx_docs.md) | [View](introduction.mdx_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `roadmap.mdx` | [View](roadmap.mdx_docs.md) | [View](roadmap.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 14: apps/docs/components


**Folder Path:** `apps/docs/components`
**Generated:** 2025-11-15T20:38:37.423330Z

---

## Overview

This directory (`apps/docs/components`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 18
- **Keyword Files:** 18

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `button.mdx` | [View](button.mdx_docs.md) | [View](button.mdx_kw.md) |
| `code-block.mdx` | [View](code-block.mdx_docs.md) | [View](code-block.mdx_kw.md) |
| `code-inline.mdx` | [View](code-inline.mdx_docs.md) | [View](code-inline.mdx_kw.md) |
| `column.mdx` | [View](column.mdx_docs.md) | [View](column.mdx_kw.md) |
| `container.mdx` | [View](container.mdx_docs.md) | [View](container.mdx_kw.md) |
| `font.mdx` | [View](font.mdx_docs.md) | [View](font.mdx_kw.md) |
| `head.mdx` | [View](head.mdx_docs.md) | [View](head.mdx_kw.md) |
| `heading.mdx` | [View](heading.mdx_docs.md) | [View](heading.mdx_kw.md) |
| `hr.mdx` | [View](hr.mdx_docs.md) | [View](hr.mdx_kw.md) |
| `html.mdx` | [View](html.mdx_docs.md) | [View](html.mdx_kw.md) |
| `image.mdx` | [View](image.mdx_docs.md) | [View](image.mdx_kw.md) |
| `link.mdx` | [View](link.mdx_docs.md) | [View](link.mdx_kw.md) |
| `markdown.mdx` | [View](markdown.mdx_docs.md) | [View](markdown.mdx_kw.md) |
| `preview.mdx` | [View](preview.mdx_docs.md) | [View](preview.mdx_kw.md) |
| `row.mdx` | [View](row.mdx_docs.md) | [View](row.mdx_kw.md) |
| `section.mdx` | [View](section.mdx_docs.md) | [View](section.mdx_kw.md) |
| `tailwind.mdx` | [View](tailwind.mdx_docs.md) | [View](tailwind.mdx_kw.md) |
| `text.mdx` | [View](text.mdx_docs.md) | [View](text.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 15: apps/docs/contributing


**Folder Path:** `apps/docs/contributing`
**Generated:** 2025-11-15T20:38:37.431509Z

---

## Overview

This directory (`apps/docs/contributing`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `development-workflow/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/contributing



| File | Documentation | Keywords |
|------|---------------|----------|
| `codebase-overview.mdx` | [View](codebase-overview.mdx_docs.md) | [View](codebase-overview.mdx_kw.md) |
| `introduction.mdx` | [View](introduction.mdx_docs.md) | [View](introduction.mdx_kw.md) |
| `opening-issues.mdx` | [View](opening-issues.mdx_docs.md) | [View](opening-issues.mdx_kw.md) |
| `opening-pull-requests.mdx` | [View](opening-pull-requests.mdx_docs.md) | [View](opening-pull-requests.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 16: apps/docs/contributing/development-workflow


**Folder Path:** `apps/docs/contributing/development-workflow`
**Generated:** 2025-11-15T20:38:37.434902Z

---

## Overview

This directory (`apps/docs/contributing/development-workflow`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 6
- **Keyword Files:** 6

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/contributing/development-workflow



| File | Documentation | Keywords |
|------|---------------|----------|
| `1-setup.mdx` | [View](1-setup.mdx_docs.md) | [View](1-setup.mdx_kw.md) |
| `2-running-tests.mdx` | [View](2-running-tests.mdx_docs.md) | [View](2-running-tests.mdx_kw.md) |
| `3-linting.mdx` | [View](3-linting.mdx_docs.md) | [View](3-linting.mdx_kw.md) |
| `4-building.mdx` | [View](4-building.mdx_docs.md) | [View](4-building.mdx_kw.md) |
| `5-writing-docs.mdx` | [View](5-writing-docs.mdx_docs.md) | [View](5-writing-docs.mdx_kw.md) |
| `6-editing-the-components.mdx` | [View](6-editing-the-components.mdx_docs.md) | [View](6-editing-the-components.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 17: apps/docs/getting-started


**Folder Path:** `apps/docs/getting-started`
**Generated:** 2025-11-15T20:38:37.437858Z

---

## Overview

This directory (`apps/docs/getting-started`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `monorepo-setup/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/getting-started



| File | Documentation | Keywords |
|------|---------------|----------|
| `automatic-setup.mdx` | [View](automatic-setup.mdx_docs.md) | [View](automatic-setup.mdx_kw.md) |
| `manual-setup.mdx` | [View](manual-setup.mdx_docs.md) | [View](manual-setup.mdx_kw.md) |
| `migrating-to-react-email.mdx` | [View](migrating-to-react-email.mdx_docs.md) | [View](migrating-to-react-email.mdx_kw.md) |
| `updating-react-email.mdx` | [View](updating-react-email.mdx_docs.md) | [View](updating-react-email.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 18: apps/docs/getting-started/monorepo-setup


**Folder Path:** `apps/docs/getting-started/monorepo-setup`
**Generated:** 2025-11-15T20:38:37.440370Z

---

## Overview

This directory (`apps/docs/getting-started/monorepo-setup`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/getting-started/monorepo-setup



| File | Documentation | Keywords |
|------|---------------|----------|
| `bun.mdx` | [View](bun.mdx_docs.md) | [View](bun.mdx_kw.md) |
| `choose-package-manager.mdx` | [View](choose-package-manager.mdx_docs.md) | [View](choose-package-manager.mdx_kw.md) |
| `npm.mdx` | [View](npm.mdx_docs.md) | [View](npm.mdx_kw.md) |
| `pnpm.mdx` | [View](pnpm.mdx_docs.md) | [View](pnpm.mdx_kw.md) |
| `yarn.mdx` | [View](yarn.mdx_docs.md) | [View](yarn.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 19: apps/docs/images


**Folder Path:** `apps/docs/images`
**Generated:** 2025-11-15T20:38:37.443233Z

---

## Overview

This directory (`apps/docs/images`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/images



| File | Documentation | Keywords |
|------|---------------|----------|
| `background.png` | [View](background.png_docs.md) | - |
| `bg.png` | [View](bg.png_docs.md) | - |
| `local-dev.jpg` | [View](local-dev.jpg_docs.md) | - |
| `preview-server-vercel-settings.png` | [View](preview-server-vercel-settings.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 20: apps/docs/integrations


**Folder Path:** `apps/docs/integrations`
**Generated:** 2025-11-15T20:38:37.443971Z

---

## Overview

This directory (`apps/docs/integrations`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 9
- **Keyword Files:** 9

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/integrations



| File | Documentation | Keywords |
|------|---------------|----------|
| `aws-ses.mdx` | [View](aws-ses.mdx_docs.md) | [View](aws-ses.mdx_kw.md) |
| `mailersend.mdx` | [View](mailersend.mdx_docs.md) | [View](mailersend.mdx_kw.md) |
| `nodemailer.mdx` | [View](nodemailer.mdx_docs.md) | [View](nodemailer.mdx_kw.md) |
| `overview.mdx` | [View](overview.mdx_docs.md) | [View](overview.mdx_kw.md) |
| `plunk.mdx` | [View](plunk.mdx_docs.md) | [View](plunk.mdx_kw.md) |
| `postmark.mdx` | [View](postmark.mdx_docs.md) | [View](postmark.mdx_kw.md) |
| `resend.mdx` | [View](resend.mdx_docs.md) | [View](resend.mdx_kw.md) |
| `scaleway.mdx` | [View](scaleway.mdx_docs.md) | [View](scaleway.mdx_kw.md) |
| `sendgrid.mdx` | [View](sendgrid.mdx_docs.md) | [View](sendgrid.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 21: apps/docs/logo


**Folder Path:** `apps/docs/logo`
**Generated:** 2025-11-15T20:38:37.448519Z

---

## Overview

This directory (`apps/docs/logo`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/logo



| File | Documentation | Keywords |
|------|---------------|----------|
| `dark.svg` | [View](dark.svg_docs.md) | - |
| `light.svg` | [View](light.svg_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 22: apps/docs/snippets


**Folder Path:** `apps/docs/snippets`
**Generated:** 2025-11-15T20:38:37.449349Z

---

## Overview

This directory (`apps/docs/snippets`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/snippets



| File | Documentation | Keywords |
|------|---------------|----------|
| `integrations.mdx` | [View](integrations.mdx_docs.md) | [View](integrations.mdx_kw.md) |
| `localdev.mdx` | [View](localdev.mdx_docs.md) | [View](localdev.mdx_kw.md) |
| `next-steps.mdx` | [View](next-steps.mdx_docs.md) | [View](next-steps.mdx_kw.md) |
| `support.mdx` | [View](support.mdx_docs.md) | [View](support.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 23: apps/docs/utilities


**Folder Path:** `apps/docs/utilities`
**Generated:** 2025-11-15T20:38:37.451214Z

---

## Overview

This directory (`apps/docs/utilities`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains documentation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/docs/utilities



| File | Documentation | Keywords |
|------|---------------|----------|
| `render.mdx` | [View](render.mdx_docs.md) | [View](render.mdx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 24: apps/web


**Folder Path:** `apps/web`
**Generated:** 2025-11-15T20:38:37.452502Z

---

## Overview

This directory (`apps/web`) contains a Node.js package. source code in the `src/` subdirectory. React components. 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 9
- **Keyword Files:** 9

### Subdirectories

- `components/`
- `public/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `next.config.ts` | [View](next.config.ts_docs.md) | [View](next.config.ts_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `postcss.config.js` | [View](postcss.config.js_docs.md) | [View](postcss.config.js_kw.md) |
| `tailwind.config.js` | [View](tailwind.config.js_docs.md) | [View](tailwind.config.js_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 25: apps/web/components


**Folder Path:** `apps/web/components`
**Generated:** 2025-11-15T20:38:37.456149Z

---

## Overview

This directory (`apps/web/components`) contains test files. 

## Structure

- **Subdirectories:** 71
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `_components/`
- `article-with-image/`
- `article-with-image-as-background/`
- `article-with-image-on-right/`
- `article-with-multiple-authors/`
- `article-with-single-author/`
- `article-with-two-cards/`
- `avatars-circular/`
- `avatars-group-stacked/`
- `avatars-rounded/`
- `avatars-with-text/`
- `bento-grid/`
- `checkout/`
- `code-block-with-custom-theme/`
- `code-block-with-line-numbers/`
- `code-block-with-predefined-theme/`
- `code-block-without-theme/`
- `code-inline-with-different-colors/`
- `customer-reviews/`
- `divider-between-rows-and-columns/`
- `download-buttons/`
- `footer-with-one-column/`
- `footer-with-two-columns/`
- `four-images-in-a-grid/`
- `header-and-four-paragraphs/`
- `header-and-four-paragraphs-and-two-columns/`
- `header-and-list-items/`
- `header-and-numbered-list-items/`
- `header-and-three-centered-paragraphs/`
- `header-with-centered-menu/`
- `header-with-side-menu/`
- `header-with-social-icons/`
- `image-with-varying-sizes/`
- `images-on-horizontal-grid/`
- `images-on-vertical-grid/`
- `link-inline-with-text/`
- `list-with-image-on-left/`
- `markdown-with-container-styles/`
- `markdown-with-custom-styles/`
- `multiple-headings/`
- `one-product/`
- `one-product-with-image-on-the-left/`
- `one-row-three-columns/`
- `one-row-two-columns/`
- `rounded-image/`
- `section-with-rows-and-columns/`
- `simple-code-inline/`
- `simple-container/`
- `simple-divider/`
- `simple-heading/`
- `simple-image/`
- `simple-link/`
- `simple-list/`
- `simple-markdown/`
- `simple-pricing-table/`
- `simple-rating-survey/`
- `simple-section/`
- `simple-text/`
- `single-button/`
- `static/`
- `stats-simple/`
- `stats-stepped/`
- `survey-section/`
- `testimonial-simple-centered/`
- `testimonial-with-large-avatar/`
- `text-with-styling/`
- `three-columns-with-images/`
- `title-four-cards/`
- `title-three-cards-in-a-row/`
- `two-buttons/`
- `two-tiers-with-emphasized-tier/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `ensure-matching-variants.spec.tsx` | [View](ensure-matching-variants.spec.tsx_docs.md) | [View](ensure-matching-variants.spec.tsx_kw.md) |
| `structure.ts` | [View](structure.ts_docs.md) | [View](structure.ts_kw.md) |
| `tailwind.config.ts` | [View](tailwind.config.ts_docs.md) | [View](tailwind.config.ts_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 26: apps/web/components/_components


**Folder Path:** `apps/web/components/_components`
**Generated:** 2025-11-15T20:38:37.458585Z

---

## Overview

This directory (`apps/web/components/_components`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/_components



| File | Documentation | Keywords |
|------|---------------|----------|
| `layout.tsx` | [View](layout.tsx_docs.md) | [View](layout.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 27: apps/web/components/article-with-image


**Folder Path:** `apps/web/components/article-with-image`
**Generated:** 2025-11-15T20:38:37.459638Z

---

## Overview

This directory (`apps/web/components/article-with-image`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-image



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 28: apps/web/components/article-with-image-as-background


**Folder Path:** `apps/web/components/article-with-image-as-background`
**Generated:** 2025-11-15T20:38:37.461017Z

---

## Overview

This directory (`apps/web/components/article-with-image-as-background`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-image-as-background



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 29: apps/web/components/article-with-image-on-right


**Folder Path:** `apps/web/components/article-with-image-on-right`
**Generated:** 2025-11-15T20:38:37.462579Z

---

## Overview

This directory (`apps/web/components/article-with-image-on-right`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-image-on-right



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 30: apps/web/components/article-with-multiple-authors


**Folder Path:** `apps/web/components/article-with-multiple-authors`
**Generated:** 2025-11-15T20:38:37.464014Z

---

## Overview

This directory (`apps/web/components/article-with-multiple-authors`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-multiple-authors



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 31: apps/web/components/article-with-single-author


**Folder Path:** `apps/web/components/article-with-single-author`
**Generated:** 2025-11-15T20:38:37.465565Z

---

## Overview

This directory (`apps/web/components/article-with-single-author`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-single-author



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 32: apps/web/components/article-with-two-cards


**Folder Path:** `apps/web/components/article-with-two-cards`
**Generated:** 2025-11-15T20:38:37.467088Z

---

## Overview

This directory (`apps/web/components/article-with-two-cards`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/article-with-two-cards



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 33: apps/web/components/avatars-circular


**Folder Path:** `apps/web/components/avatars-circular`
**Generated:** 2025-11-15T20:38:37.469293Z

---

## Overview

This directory (`apps/web/components/avatars-circular`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/avatars-circular



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 34: apps/web/components/avatars-group-stacked


**Folder Path:** `apps/web/components/avatars-group-stacked`
**Generated:** 2025-11-15T20:38:37.470544Z

---

## Overview

This directory (`apps/web/components/avatars-group-stacked`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/avatars-group-stacked



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 35: apps/web/components/avatars-rounded


**Folder Path:** `apps/web/components/avatars-rounded`
**Generated:** 2025-11-15T20:38:37.471869Z

---

## Overview

This directory (`apps/web/components/avatars-rounded`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/avatars-rounded



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 36: apps/web/components/avatars-with-text


**Folder Path:** `apps/web/components/avatars-with-text`
**Generated:** 2025-11-15T20:38:37.473192Z

---

## Overview

This directory (`apps/web/components/avatars-with-text`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/avatars-with-text



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 37: apps/web/components/bento-grid


**Folder Path:** `apps/web/components/bento-grid`
**Generated:** 2025-11-15T20:38:37.474625Z

---

## Overview

This directory (`apps/web/components/bento-grid`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/bento-grid



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 38: apps/web/components/checkout


**Folder Path:** `apps/web/components/checkout`
**Generated:** 2025-11-15T20:38:37.476379Z

---

## Overview

This directory (`apps/web/components/checkout`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/checkout



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 39: apps/web/components/code-block-with-custom-theme


**Folder Path:** `apps/web/components/code-block-with-custom-theme`
**Generated:** 2025-11-15T20:38:37.477853Z

---

## Overview

This directory (`apps/web/components/code-block-with-custom-theme`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/code-block-with-custom-theme



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 40: apps/web/components/code-block-with-line-numbers


**Folder Path:** `apps/web/components/code-block-with-line-numbers`
**Generated:** 2025-11-15T20:38:37.479065Z

---

## Overview

This directory (`apps/web/components/code-block-with-line-numbers`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/code-block-with-line-numbers



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 41: apps/web/components/code-block-with-predefined-theme


**Folder Path:** `apps/web/components/code-block-with-predefined-theme`
**Generated:** 2025-11-15T20:38:37.480128Z

---

## Overview

This directory (`apps/web/components/code-block-with-predefined-theme`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/code-block-with-predefined-theme



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 42: apps/web/components/code-block-without-theme


**Folder Path:** `apps/web/components/code-block-without-theme`
**Generated:** 2025-11-15T20:38:37.481154Z

---

## Overview

This directory (`apps/web/components/code-block-without-theme`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/code-block-without-theme



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 43: apps/web/components/code-inline-with-different-colors


**Folder Path:** `apps/web/components/code-inline-with-different-colors`
**Generated:** 2025-11-15T20:38:37.482300Z

---

## Overview

This directory (`apps/web/components/code-inline-with-different-colors`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/code-inline-with-different-colors



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 44: apps/web/components/customer-reviews


**Folder Path:** `apps/web/components/customer-reviews`
**Generated:** 2025-11-15T20:38:37.483706Z

---

## Overview

This directory (`apps/web/components/customer-reviews`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/customer-reviews



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 45: apps/web/components/divider-between-rows-and-columns


**Folder Path:** `apps/web/components/divider-between-rows-and-columns`
**Generated:** 2025-11-15T20:38:37.485481Z

---

## Overview

This directory (`apps/web/components/divider-between-rows-and-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/divider-between-rows-and-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 46: apps/web/components/download-buttons


**Folder Path:** `apps/web/components/download-buttons`
**Generated:** 2025-11-15T20:38:37.486829Z

---

## Overview

This directory (`apps/web/components/download-buttons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/download-buttons



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 47: apps/web/components/footer-with-one-column


**Folder Path:** `apps/web/components/footer-with-one-column`
**Generated:** 2025-11-15T20:38:37.488163Z

---

## Overview

This directory (`apps/web/components/footer-with-one-column`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/footer-with-one-column



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 48: apps/web/components/footer-with-two-columns


**Folder Path:** `apps/web/components/footer-with-two-columns`
**Generated:** 2025-11-15T20:38:37.489504Z

---

## Overview

This directory (`apps/web/components/footer-with-two-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/footer-with-two-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 49: apps/web/components/four-images-in-a-grid


**Folder Path:** `apps/web/components/four-images-in-a-grid`
**Generated:** 2025-11-15T20:38:37.490930Z

---

## Overview

This directory (`apps/web/components/four-images-in-a-grid`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/four-images-in-a-grid



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 50: apps/web/components/header-and-four-paragraphs


**Folder Path:** `apps/web/components/header-and-four-paragraphs`
**Generated:** 2025-11-15T20:38:37.492421Z

---

## Overview

This directory (`apps/web/components/header-and-four-paragraphs`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-and-four-paragraphs



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 51: apps/web/components/header-and-four-paragraphs-and-two-columns


**Folder Path:** `apps/web/components/header-and-four-paragraphs-and-two-columns`
**Generated:** 2025-11-15T20:38:37.494117Z

---

## Overview

This directory (`apps/web/components/header-and-four-paragraphs-and-two-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-and-four-paragraphs-and-two-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 52: apps/web/components/header-and-list-items


**Folder Path:** `apps/web/components/header-and-list-items`
**Generated:** 2025-11-15T20:38:37.495754Z

---

## Overview

This directory (`apps/web/components/header-and-list-items`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-and-list-items



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 53: apps/web/components/header-and-numbered-list-items


**Folder Path:** `apps/web/components/header-and-numbered-list-items`
**Generated:** 2025-11-15T20:38:37.497199Z

---

## Overview

This directory (`apps/web/components/header-and-numbered-list-items`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-and-numbered-list-items



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 54: apps/web/components/header-and-three-centered-paragraphs


**Folder Path:** `apps/web/components/header-and-three-centered-paragraphs`
**Generated:** 2025-11-15T20:38:37.498713Z

---

## Overview

This directory (`apps/web/components/header-and-three-centered-paragraphs`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-and-three-centered-paragraphs



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 55: apps/web/components/header-with-centered-menu


**Folder Path:** `apps/web/components/header-with-centered-menu`
**Generated:** 2025-11-15T20:38:37.500353Z

---

## Overview

This directory (`apps/web/components/header-with-centered-menu`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-with-centered-menu



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 56: apps/web/components/header-with-side-menu


**Folder Path:** `apps/web/components/header-with-side-menu`
**Generated:** 2025-11-15T20:38:37.501680Z

---

## Overview

This directory (`apps/web/components/header-with-side-menu`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-with-side-menu



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 57: apps/web/components/header-with-social-icons


**Folder Path:** `apps/web/components/header-with-social-icons`
**Generated:** 2025-11-15T20:38:37.503035Z

---

## Overview

This directory (`apps/web/components/header-with-social-icons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/header-with-social-icons



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 58: apps/web/components/image-with-varying-sizes


**Folder Path:** `apps/web/components/image-with-varying-sizes`
**Generated:** 2025-11-15T20:38:37.504240Z

---

## Overview

This directory (`apps/web/components/image-with-varying-sizes`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/image-with-varying-sizes



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 59: apps/web/components/images-on-horizontal-grid


**Folder Path:** `apps/web/components/images-on-horizontal-grid`
**Generated:** 2025-11-15T20:38:37.505418Z

---

## Overview

This directory (`apps/web/components/images-on-horizontal-grid`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/images-on-horizontal-grid



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 60: apps/web/components/images-on-vertical-grid


**Folder Path:** `apps/web/components/images-on-vertical-grid`
**Generated:** 2025-11-15T20:38:37.507043Z

---

## Overview

This directory (`apps/web/components/images-on-vertical-grid`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/images-on-vertical-grid



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 61: apps/web/components/link-inline-with-text


**Folder Path:** `apps/web/components/link-inline-with-text`
**Generated:** 2025-11-15T20:38:37.508760Z

---

## Overview

This directory (`apps/web/components/link-inline-with-text`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/link-inline-with-text



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 62: apps/web/components/list-with-image-on-left


**Folder Path:** `apps/web/components/list-with-image-on-left`
**Generated:** 2025-11-15T20:38:37.509946Z

---

## Overview

This directory (`apps/web/components/list-with-image-on-left`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/list-with-image-on-left



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 63: apps/web/components/markdown-with-container-styles


**Folder Path:** `apps/web/components/markdown-with-container-styles`
**Generated:** 2025-11-15T20:38:37.511550Z

---

## Overview

This directory (`apps/web/components/markdown-with-container-styles`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/markdown-with-container-styles



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 64: apps/web/components/markdown-with-custom-styles


**Folder Path:** `apps/web/components/markdown-with-custom-styles`
**Generated:** 2025-11-15T20:38:37.512552Z

---

## Overview

This directory (`apps/web/components/markdown-with-custom-styles`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/markdown-with-custom-styles



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 65: apps/web/components/multiple-headings


**Folder Path:** `apps/web/components/multiple-headings`
**Generated:** 2025-11-15T20:38:37.513482Z

---

## Overview

This directory (`apps/web/components/multiple-headings`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/multiple-headings



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 66: apps/web/components/one-product


**Folder Path:** `apps/web/components/one-product`
**Generated:** 2025-11-15T20:38:37.514836Z

---

## Overview

This directory (`apps/web/components/one-product`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/one-product



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 67: apps/web/components/one-product-with-image-on-the-left


**Folder Path:** `apps/web/components/one-product-with-image-on-the-left`
**Generated:** 2025-11-15T20:38:37.516211Z

---

## Overview

This directory (`apps/web/components/one-product-with-image-on-the-left`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/one-product-with-image-on-the-left



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 68: apps/web/components/one-row-three-columns


**Folder Path:** `apps/web/components/one-row-three-columns`
**Generated:** 2025-11-15T20:38:37.517673Z

---

## Overview

This directory (`apps/web/components/one-row-three-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/one-row-three-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 69: apps/web/components/one-row-two-columns


**Folder Path:** `apps/web/components/one-row-two-columns`
**Generated:** 2025-11-15T20:38:37.519186Z

---

## Overview

This directory (`apps/web/components/one-row-two-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/one-row-two-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 70: apps/web/components/rounded-image


**Folder Path:** `apps/web/components/rounded-image`
**Generated:** 2025-11-15T20:38:37.520462Z

---

## Overview

This directory (`apps/web/components/rounded-image`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/rounded-image



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 71: apps/web/components/section-with-rows-and-columns


**Folder Path:** `apps/web/components/section-with-rows-and-columns`
**Generated:** 2025-11-15T20:38:37.521766Z

---

## Overview

This directory (`apps/web/components/section-with-rows-and-columns`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/section-with-rows-and-columns



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 72: apps/web/components/simple-code-inline


**Folder Path:** `apps/web/components/simple-code-inline`
**Generated:** 2025-11-15T20:38:37.522771Z

---

## Overview

This directory (`apps/web/components/simple-code-inline`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-code-inline



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 73: apps/web/components/simple-container


**Folder Path:** `apps/web/components/simple-container`
**Generated:** 2025-11-15T20:38:37.523969Z

---

## Overview

This directory (`apps/web/components/simple-container`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-container



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 74: apps/web/components/simple-divider


**Folder Path:** `apps/web/components/simple-divider`
**Generated:** 2025-11-15T20:38:37.525222Z

---

## Overview

This directory (`apps/web/components/simple-divider`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-divider



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 75: apps/web/components/simple-heading


**Folder Path:** `apps/web/components/simple-heading`
**Generated:** 2025-11-15T20:38:37.526404Z

---

## Overview

This directory (`apps/web/components/simple-heading`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-heading



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 76: apps/web/components/simple-image


**Folder Path:** `apps/web/components/simple-image`
**Generated:** 2025-11-15T20:38:37.527637Z

---

## Overview

This directory (`apps/web/components/simple-image`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-image



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 77: apps/web/components/simple-link


**Folder Path:** `apps/web/components/simple-link`
**Generated:** 2025-11-15T20:38:37.529148Z

---

## Overview

This directory (`apps/web/components/simple-link`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-link



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 78: apps/web/components/simple-list


**Folder Path:** `apps/web/components/simple-list`
**Generated:** 2025-11-15T20:38:37.530204Z

---

## Overview

This directory (`apps/web/components/simple-list`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-list



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 79: apps/web/components/simple-markdown


**Folder Path:** `apps/web/components/simple-markdown`
**Generated:** 2025-11-15T20:38:37.531746Z

---

## Overview

This directory (`apps/web/components/simple-markdown`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-markdown



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 80: apps/web/components/simple-pricing-table


**Folder Path:** `apps/web/components/simple-pricing-table`
**Generated:** 2025-11-15T20:38:37.532772Z

---

## Overview

This directory (`apps/web/components/simple-pricing-table`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-pricing-table



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 81: apps/web/components/simple-rating-survey


**Folder Path:** `apps/web/components/simple-rating-survey`
**Generated:** 2025-11-15T20:38:37.534558Z

---

## Overview

This directory (`apps/web/components/simple-rating-survey`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-rating-survey



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 82: apps/web/components/simple-section


**Folder Path:** `apps/web/components/simple-section`
**Generated:** 2025-11-15T20:38:37.536168Z

---

## Overview

This directory (`apps/web/components/simple-section`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-section



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 83: apps/web/components/simple-text


**Folder Path:** `apps/web/components/simple-text`
**Generated:** 2025-11-15T20:38:37.537253Z

---

## Overview

This directory (`apps/web/components/simple-text`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/simple-text



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 84: apps/web/components/single-button


**Folder Path:** `apps/web/components/single-button`
**Generated:** 2025-11-15T20:38:37.538587Z

---

## Overview

This directory (`apps/web/components/single-button`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/single-button



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 85: apps/web/components/static


**Folder Path:** `apps/web/components/static`
**Generated:** 2025-11-15T20:38:37.540484Z

---

## Overview

This directory (`apps/web/components/static`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 35
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/static



| File | Documentation | Keywords |
|------|---------------|----------|
| `atmos-vacuum-canister.jpg` | [View](atmos-vacuum-canister.jpg_docs.md) | - |
| `braun-analogue-clock.jpg` | [View](braun-analogue-clock.jpg_docs.md) | - |
| `braun-classic-watch.jpg` | [View](braun-classic-watch.jpg_docs.md) | - |
| `braun-collection.jpg` | [View](braun-collection.jpg_docs.md) | - |
| `braun-vintage.jpg` | [View](braun-vintage.jpg_docs.md) | - |
| `braun-wall-clock.jpg` | [View](braun-wall-clock.jpg_docs.md) | - |
| `braun-wireless-alarm.jpg` | [View](braun-wireless-alarm.jpg_docs.md) | - |
| `bundle-collection.jpg` | [View](bundle-collection.jpg_docs.md) | - |
| `clara-french-press.jpg` | [View](clara-french-press.jpg_docs.md) | - |
| `clyde-electric-kettle.jpg` | [View](clyde-electric-kettle.jpg_docs.md) | - |
| `coffee-bean-storage.jpg` | [View](coffee-bean-storage.jpg_docs.md) | - |
| `cube-icon.png` | [View](cube-icon.png_docs.md) | - |
| `download-on-the-app-store.png` | [View](download-on-the-app-store.png_docs.md) | - |
| `facebook-logo.png` | [View](facebook-logo.png_docs.md) | - |
| `get-it-on-google-play.png` | [View](get-it-on-google-play.png_docs.md) | - |
| `grinder-collection.jpg` | [View](grinder-collection.jpg_docs.md) | - |
| `heart-icon.png` | [View](heart-icon.png_docs.md) | - |
| `herman-miller-chair.jpg` | [View](herman-miller-chair.jpg_docs.md) | - |
| `in-icon.png` | [View](in-icon.png_docs.md) | - |
| `instagram-logo.png` | [View](instagram-logo.png_docs.md) | - |
| `logo-without-background.png` | [View](logo-without-background.png_docs.md) | - |
| `megaphone-icon.png` | [View](megaphone-icon.png_docs.md) | - |
| `monty-art-cup-1.jpg` | [View](monty-art-cup-1.jpg_docs.md) | - |
| `monty-art-cup-2.jpg` | [View](monty-art-cup-2.jpg_docs.md) | - |
| `mugs-collection.jpg` | [View](mugs-collection.jpg_docs.md) | - |
| `ode-grinder.jpg` | [View](ode-grinder.jpg_docs.md) | - |
| `outdoor-living.jpg` | [View](outdoor-living.jpg_docs.md) | - |
| `rocket-icon.png` | [View](rocket-icon.png_docs.md) | - |
| `stagg-eletric-kettle.jpg` | [View](stagg-eletric-kettle.jpg_docs.md) | - |
| `steve-jobs.jpg` | [View](steve-jobs.jpg_docs.md) | - |
| `steve-wozniak.jpg` | [View](steve-wozniak.jpg_docs.md) | - |
| `vacuum-canister-clear-glass-bundle.jpg` | [View](vacuum-canister-clear-glass-bundle.jpg_docs.md) | - |
| `versatile-comfort.jpg` | [View](versatile-comfort.jpg_docs.md) | - |
| `x-icon.png` | [View](x-icon.png_docs.md) | - |
| `x-logo.png` | [View](x-logo.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 86: apps/web/components/stats-simple


**Folder Path:** `apps/web/components/stats-simple`
**Generated:** 2025-11-15T20:38:37.541243Z

---

## Overview

This directory (`apps/web/components/stats-simple`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/stats-simple



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 87: apps/web/components/stats-stepped


**Folder Path:** `apps/web/components/stats-stepped`
**Generated:** 2025-11-15T20:38:37.542713Z

---

## Overview

This directory (`apps/web/components/stats-stepped`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/stats-stepped



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 88: apps/web/components/survey-section


**Folder Path:** `apps/web/components/survey-section`
**Generated:** 2025-11-15T20:38:37.544252Z

---

## Overview

This directory (`apps/web/components/survey-section`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/survey-section



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 89: apps/web/components/testimonial-simple-centered


**Folder Path:** `apps/web/components/testimonial-simple-centered`
**Generated:** 2025-11-15T20:38:37.545709Z

---

## Overview

This directory (`apps/web/components/testimonial-simple-centered`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains test files for validating functionality.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/testimonial-simple-centered



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 90: apps/web/components/testimonial-with-large-avatar


**Folder Path:** `apps/web/components/testimonial-with-large-avatar`
**Generated:** 2025-11-15T20:38:37.547282Z

---

## Overview

This directory (`apps/web/components/testimonial-with-large-avatar`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains test files for validating functionality.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/testimonial-with-large-avatar



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 91: apps/web/components/text-with-styling


**Folder Path:** `apps/web/components/text-with-styling`
**Generated:** 2025-11-15T20:38:37.548874Z

---

## Overview

This directory (`apps/web/components/text-with-styling`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/text-with-styling



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 92: apps/web/components/three-columns-with-images


**Folder Path:** `apps/web/components/three-columns-with-images`
**Generated:** 2025-11-15T20:38:37.550147Z

---

## Overview

This directory (`apps/web/components/three-columns-with-images`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/three-columns-with-images



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 93: apps/web/components/title-four-cards


**Folder Path:** `apps/web/components/title-four-cards`
**Generated:** 2025-11-15T20:38:37.551619Z

---

## Overview

This directory (`apps/web/components/title-four-cards`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/title-four-cards



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 94: apps/web/components/title-three-cards-in-a-row


**Folder Path:** `apps/web/components/title-three-cards-in-a-row`
**Generated:** 2025-11-15T20:38:37.553291Z

---

## Overview

This directory (`apps/web/components/title-three-cards-in-a-row`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/title-three-cards-in-a-row



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 95: apps/web/components/two-buttons


**Folder Path:** `apps/web/components/two-buttons`
**Generated:** 2025-11-15T20:38:37.555128Z

---

## Overview

This directory (`apps/web/components/two-buttons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/two-buttons



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 96: apps/web/components/two-tiers-with-emphasized-tier


**Folder Path:** `apps/web/components/two-tiers-with-emphasized-tier`
**Generated:** 2025-11-15T20:38:37.556665Z

---

## Overview

This directory (`apps/web/components/two-tiers-with-emphasized-tier`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/components/two-tiers-with-emphasized-tier



| File | Documentation | Keywords |
|------|---------------|----------|
| `inline-styles.tsx` | [View](inline-styles.tsx_docs.md) | [View](inline-styles.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 97: apps/web/public


**Folder Path:** `apps/web/public`
**Generated:** 2025-11-15T20:38:37.558292Z

---

## Overview

This directory (`apps/web/public`) contains 

## Structure

- **Subdirectories:** 6
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `brand/`
- `examples/`
- `fonts/`
- `js/`
- `meta/`
- `static/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public

---

# Chapter 98: apps/web/public/brand


**Folder Path:** `apps/web/public/brand`
**Generated:** 2025-11-15T20:38:37.558997Z

---

## Overview

This directory (`apps/web/public/brand`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/brand



| File | Documentation | Keywords |
|------|---------------|----------|
| `example-logo.png` | [View](example-logo.png_docs.md) | - |
| `logo-without-background.png` | [View](logo-without-background.png_docs.md) | - |
| `logo.png` | [View](logo.png_docs.md) | - |
| `resend.png` | [View](resend.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 99: apps/web/public/examples


**Folder Path:** `apps/web/public/examples`
**Generated:** 2025-11-15T20:38:37.559730Z

---

## Overview

This directory (`apps/web/public/examples`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 19
- **Keyword Files:** 0

### Subdirectories

- `authors/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/examples



| File | Documentation | Keywords |
|------|---------------|----------|
| `airbnb-review.png` | [View](airbnb-review.png_docs.md) | - |
| `apple-receipt.png` | [View](apple-receipt.png_docs.md) | - |
| `aws-verify-email.png` | [View](aws-verify-email.png_docs.md) | - |
| `demo.png` | [View](demo.png_docs.md) | - |
| `dropbox-reset-password.png` | [View](dropbox-reset-password.png_docs.md) | - |
| `github-access-token.png` | [View](github-access-token.png_docs.md) | - |
| `google-play-policy-update.png` | [View](google-play-policy-update.png_docs.md) | - |
| `koala-welcome.png` | [View](koala-welcome.png_docs.md) | - |
| `linear-login-code.png` | [View](linear-login-code.png_docs.md) | - |
| `nike-receipt.png` | [View](nike-receipt.png_docs.md) | - |
| `notion-magic-link.png` | [View](notion-magic-link.png_docs.md) | - |
| `plaid-verify-identity.png` | [View](plaid-verify-identity.png_docs.md) | - |
| `raycast-magic-link.png` | [View](raycast-magic-link.png_docs.md) | - |
| `slack-confirm.png` | [View](slack-confirm.png_docs.md) | - |
| `stack-overflow-tips.png` | [View](stack-overflow-tips.png_docs.md) | - |
| `stripe-welcome.png` | [View](stripe-welcome.png_docs.md) | - |
| `twitch-reset-password.png` | [View](twitch-reset-password.png_docs.md) | - |
| `vercel-invite-user.png` | [View](vercel-invite-user.png_docs.md) | - |
| `yelp-recent-login.png` | [View](yelp-recent-login.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 100: apps/web/public/examples/authors


**Folder Path:** `apps/web/public/examples/authors`
**Generated:** 2025-11-15T20:38:37.560481Z

---

## Overview

This directory (`apps/web/public/examples/authors`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 13
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/examples/authors



| File | Documentation | Keywords |
|------|---------------|----------|
| `EmersonGarrido.png` | [View](EmersonGarrido.png_docs.md) | - |
| `Rychillie.png` | [View](Rychillie.png_docs.md) | - |
| `abhinandanwadwa.png` | [View](abhinandanwadwa.png_docs.md) | - |
| `bruno88cabral.png` | [View](bruno88cabral.png_docs.md) | - |
| `bukinoshita.png` | [View](bukinoshita.png_docs.md) | - |
| `c0dr.png` | [View](c0dr.png_docs.md) | - |
| `camillegachido.png` | [View](camillegachido.png_docs.md) | - |
| `joaom00.png` | [View](joaom00.png_docs.md) | - |
| `nettofarah.png` | [View](nettofarah.png_docs.md) | - |
| `relferreira.png` | [View](relferreira.png_docs.md) | - |
| `ribeiroevandro.png` | [View](ribeiroevandro.png_docs.md) | - |
| `thecodeinfluencer.png` | [View](thecodeinfluencer.png_docs.md) | - |
| `zenorocha.png` | [View](zenorocha.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 101: apps/web/public/fonts


**Folder Path:** `apps/web/public/fonts`
**Generated:** 2025-11-15T20:38:37.561343Z

---

## Overview

This directory (`apps/web/public/fonts`) contains 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `commit-mono/`
- `inter/`
- `shantell-sans/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/fonts

---

# Chapter 102: apps/web/public/fonts/commit-mono


**Folder Path:** `apps/web/public/fonts/commit-mono`
**Generated:** 2025-11-15T20:38:37.562057Z

---

## Overview

This directory (`apps/web/public/fonts/commit-mono`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/fonts/commit-mono



| File | Documentation | Keywords |
|------|---------------|----------|
| `commit-mono-italic.ttf` | [View](commit-mono-italic.ttf_docs.md) | - |
| `commit-mono-regular.ttf` | [View](commit-mono-regular.ttf_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 103: apps/web/public/fonts/inter


**Folder Path:** `apps/web/public/fonts/inter`
**Generated:** 2025-11-15T20:38:37.562845Z

---

## Overview

This directory (`apps/web/public/fonts/inter`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/fonts/inter



| File | Documentation | Keywords |
|------|---------------|----------|
| `inter.ttf` | [View](inter.ttf_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 104: apps/web/public/fonts/shantell-sans


**Folder Path:** `apps/web/public/fonts/shantell-sans`
**Generated:** 2025-11-15T20:38:37.563561Z

---

## Overview

This directory (`apps/web/public/fonts/shantell-sans`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/fonts/shantell-sans



| File | Documentation | Keywords |
|------|---------------|----------|
| `shantell-sans-italic.ttf` | [View](shantell-sans-italic.ttf_docs.md) | - |
| `shantell-sans-regular.ttf` | [View](shantell-sans-regular.ttf_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 105: apps/web/public/js


**Folder Path:** `apps/web/public/js`
**Generated:** 2025-11-15T20:38:37.564382Z

---

## Overview

This directory (`apps/web/public/js`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/js



| File | Documentation | Keywords |
|------|---------------|----------|
| `web-streams-polyfill.js` | [View](web-streams-polyfill.js_docs.md) | [View](web-streams-polyfill.js_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 106: apps/web/public/meta


**Folder Path:** `apps/web/public/meta`
**Generated:** 2025-11-15T20:38:37.567399Z

---

## Overview

This directory (`apps/web/public/meta`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/meta



| File | Documentation | Keywords |
|------|---------------|----------|
| `apple-touch-icon.png` | [View](apple-touch-icon.png_docs.md) | - |
| `cover.png` | [View](cover.png_docs.md) | - |
| `favicon.ico` | [View](favicon.ico_docs.md) | - |
| `favicon.svg` | [View](favicon.svg_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 107: apps/web/public/static


**Folder Path:** `apps/web/public/static`
**Generated:** 2025-11-15T20:38:37.568422Z

---

## Overview

This directory (`apps/web/public/static`) contains React components. 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 40
- **Keyword Files:** 0

### Subdirectories

- `components/`
- `covers/`
- `icons/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/static



| File | Documentation | Keywords |
|------|---------------|----------|
| `atmos-vacuum-canister.jpg` | [View](atmos-vacuum-canister.jpg_docs.md) | - |
| `bg.png` | [View](bg.png_docs.md) | - |
| `braun-analogue-clock.jpg` | [View](braun-analogue-clock.jpg_docs.md) | - |
| `braun-classic-watch.jpg` | [View](braun-classic-watch.jpg_docs.md) | - |
| `braun-collection.jpg` | [View](braun-collection.jpg_docs.md) | - |
| `braun-vintage.jpg` | [View](braun-vintage.jpg_docs.md) | - |
| `braun-wall-clock.jpg` | [View](braun-wall-clock.jpg_docs.md) | - |
| `braun-wireless-alarm.jpg` | [View](braun-wireless-alarm.jpg_docs.md) | - |
| `bundle-collection.jpg` | [View](bundle-collection.jpg_docs.md) | - |
| `clara-french-press.jpg` | [View](clara-french-press.jpg_docs.md) | - |
| `clyde-electric-kettle.jpg` | [View](clyde-electric-kettle.jpg_docs.md) | - |
| `coffee-bean-storage.jpg` | [View](coffee-bean-storage.jpg_docs.md) | - |
| `cube-icon.png` | [View](cube-icon.png_docs.md) | - |
| `demo-example.png` | [View](demo-example.png_docs.md) | - |
| `download-on-the-app-store.png` | [View](download-on-the-app-store.png_docs.md) | - |
| `facebook-logo.png` | [View](facebook-logo.png_docs.md) | - |
| `get-it-on-google-play.png` | [View](get-it-on-google-play.png_docs.md) | - |
| `gmail.svg` | [View](gmail.svg_docs.md) | - |
| `grinder-collection.jpg` | [View](grinder-collection.jpg_docs.md) | - |
| `heart-icon.png` | [View](heart-icon.png_docs.md) | - |
| `herman-miller-chair.jpg` | [View](herman-miller-chair.jpg_docs.md) | - |
| `in-icon.png` | [View](in-icon.png_docs.md) | - |
| `instagram-logo.png` | [View](instagram-logo.png_docs.md) | - |
| `lee-robinson.jpg` | [View](lee-robinson.jpg_docs.md) | - |
| `logo-without-background.png` | [View](logo-without-background.png_docs.md) | - |
| `megaphone-icon.png` | [View](megaphone-icon.png_docs.md) | - |
| `monty-art-cup-1.jpg` | [View](monty-art-cup-1.jpg_docs.md) | - |
| `monty-art-cup-2.jpg` | [View](monty-art-cup-2.jpg_docs.md) | - |
| `mugs-collection.jpg` | [View](mugs-collection.jpg_docs.md) | - |
| `ode-grinder.jpg` | [View](ode-grinder.jpg_docs.md) | - |
| `outdoor-living.jpg` | [View](outdoor-living.jpg_docs.md) | - |
| `resend-wallpaper.jpg` | [View](resend-wallpaper.jpg_docs.md) | - |
| `rocket-icon.png` | [View](rocket-icon.png_docs.md) | - |
| `stagg-eletric-kettle.jpg` | [View](stagg-eletric-kettle.jpg_docs.md) | - |
| `steve-jobs.jpg` | [View](steve-jobs.jpg_docs.md) | - |
| `steve-wozniak.jpg` | [View](steve-wozniak.jpg_docs.md) | - |
| `vacuum-canister-clear-glass-bundle.jpg` | [View](vacuum-canister-clear-glass-bundle.jpg_docs.md) | - |
| `versatile-comfort.jpg` | [View](versatile-comfort.jpg_docs.md) | - |
| `x-icon.png` | [View](x-icon.png_docs.md) | - |
| `x-logo.png` | [View](x-logo.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 108: apps/web/public/static/components


**Folder Path:** `apps/web/public/static/components`
**Generated:** 2025-11-15T20:38:37.569189Z

---

## Overview

This directory (`apps/web/public/static/components`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/static/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `0.jpeg` | [View](0.jpeg_docs.md) | - |
| `1.jpeg` | [View](1.jpeg_docs.md) | - |
| `2.jpeg` | [View](2.jpeg_docs.md) | - |
| `3.jpeg` | [View](3.jpeg_docs.md) | - |
| `4.jpeg` | [View](4.jpeg_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 109: apps/web/public/static/covers


**Folder Path:** `apps/web/public/static/covers`
**Generated:** 2025-11-15T20:38:37.570192Z

---

## Overview

This directory (`apps/web/public/static/covers`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 23
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/static/covers



| File | Documentation | Keywords |
|------|---------------|----------|
| `button.png` | [View](button.png_docs.md) | - |
| `code-block.png` | [View](code-block.png_docs.md) | - |
| `code-inline.png` | [View](code-inline.png_docs.md) | - |
| `column.png` | [View](column.png_docs.md) | - |
| `components.png` | [View](components.png_docs.md) | - |
| `container.png` | [View](container.png_docs.md) | - |
| `create-email.png` | [View](create-email.png_docs.md) | - |
| `font.png` | [View](font.png_docs.md) | - |
| `head.png` | [View](head.png_docs.md) | - |
| `heading.png` | [View](heading.png_docs.md) | - |
| `hr.png` | [View](hr.png_docs.md) | - |
| `html.png` | [View](html.png_docs.md) | - |
| `img.png` | [View](img.png_docs.md) | - |
| `link.png` | [View](link.png_docs.md) | - |
| `markdown.png` | [View](markdown.png_docs.md) | - |
| `patterns.png` | [View](patterns.png_docs.md) | - |
| `preview.png` | [View](preview.png_docs.md) | - |
| `react-email.png` | [View](react-email.png_docs.md) | - |
| `render.png` | [View](render.png_docs.md) | - |
| `row.png` | [View](row.png_docs.md) | - |
| `section.png` | [View](section.png_docs.md) | - |
| `tailwind.png` | [View](tailwind.png_docs.md) | - |
| `text.png` | [View](text.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 110: apps/web/public/static/icons


**Folder Path:** `apps/web/public/static/icons`
**Generated:** 2025-11-15T20:38:37.570990Z

---

## Overview

This directory (`apps/web/public/static/icons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 6
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/public/static/icons



| File | Documentation | Keywords |
|------|---------------|----------|
| `apple-mail.svg` | [View](apple-mail.svg_docs.md) | - |
| `gmail.svg` | [View](gmail.svg_docs.md) | - |
| `hey.svg` | [View](hey.svg_docs.md) | - |
| `outlook.svg` | [View](outlook.svg_docs.md) | - |
| `superhuman.svg` | [View](superhuman.svg_docs.md) | - |
| `yahoo-mail.svg` | [View](yahoo-mail.svg_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 111: apps/web/src


**Folder Path:** `apps/web/src`
**Generated:** 2025-11-15T20:38:37.571697Z

---

## Overview

This directory (`apps/web/src`) contains React components. 

## Structure

- **Subdirectories:** 8
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `app/`
- `components/`
- `hooks/`
- `illustrations/`
- `styles/`
- `types/`
- `utils/`
- `webgl/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src

---

# Chapter 112: apps/web/src/app


**Folder Path:** `apps/web/src/app`
**Generated:** 2025-11-15T20:38:37.572346Z

---

## Overview

This directory (`apps/web/src/app`) contains React components. 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `api/`
- `components/`
- `templates/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app



| File | Documentation | Keywords |
|------|---------------|----------|
| `layout.tsx` | [View](layout.tsx_docs.md) | [View](layout.tsx_kw.md) |
| `not-found.tsx` | [View](not-found.tsx_docs.md) | [View](not-found.tsx_kw.md) |
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |
| `robots.ts` | [View](robots.ts_docs.md) | [View](robots.ts_kw.md) |
| `sitemap.ts` | [View](sitemap.ts_docs.md) | [View](sitemap.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 113: apps/web/src/app/api


**Folder Path:** `apps/web/src/app/api`
**Generated:** 2025-11-15T20:38:37.574697Z

---

## Overview

This directory (`apps/web/src/app/api`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `check-spam/`
- `send/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api

---

# Chapter 114: apps/web/src/app/api/check-spam


**Folder Path:** `apps/web/src/app/api/check-spam`
**Generated:** 2025-11-15T20:38:37.575440Z

---

## Overview

This directory (`apps/web/src/app/api/check-spam`) contains test files. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `testing/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api/check-spam



| File | Documentation | Keywords |
|------|---------------|----------|
| `check-spam.spec.tsx` | [View](check-spam.spec.tsx_docs.md) | [View](check-spam.spec.tsx_kw.md) |
| `check-spam.ts` | [View](check-spam.ts_docs.md) | [View](check-spam.ts_kw.md) |
| `route.ts` | [View](route.ts_docs.md) | [View](route.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 115: apps/web/src/app/api/check-spam/__snapshots__


**Folder Path:** `apps/web/src/app/api/check-spam/__snapshots__`
**Generated:** 2025-11-15T20:38:37.577282Z

---

## Overview

This directory (`apps/web/src/app/api/check-spam/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api/check-spam/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `check-spam.spec.tsx.snap` | [View](check-spam.spec.tsx.snap_docs.md) | [View](check-spam.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 116: apps/web/src/app/api/check-spam/testing


**Folder Path:** `apps/web/src/app/api/check-spam/testing`
**Generated:** 2025-11-15T20:38:37.578499Z

---

## Overview

This directory (`apps/web/src/app/api/check-spam/testing`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api/check-spam/testing



| File | Documentation | Keywords |
|------|---------------|----------|
| `stripe-welcome-email.tsx` | [View](stripe-welcome-email.tsx_docs.md) | [View](stripe-welcome-email.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 117: apps/web/src/app/api/send


**Folder Path:** `apps/web/src/app/api/send`
**Generated:** 2025-11-15T20:38:37.580227Z

---

## Overview

This directory (`apps/web/src/app/api/send`) contains test files. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `test/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api/send

---

# Chapter 118: apps/web/src/app/api/send/test


**Folder Path:** `apps/web/src/app/api/send/test`
**Generated:** 2025-11-15T20:38:37.581202Z

---

## Overview

This directory (`apps/web/src/app/api/send/test`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/api/send/test



| File | Documentation | Keywords |
|------|---------------|----------|
| `route.ts` | [View](route.ts_docs.md) | [View](route.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 119: apps/web/src/app/components


**Folder Path:** `apps/web/src/app/components`
**Generated:** 2025-11-15T20:38:37.582774Z

---

## Overview

This directory (`apps/web/src/app/components`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `[slug]/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-imported-components-for.tsx` | [View](get-imported-components-for.tsx_docs.md) | [View](get-imported-components-for.tsx_kw.md) |
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 120: apps/web/src/app/components/[slug]


**Folder Path:** `apps/web/src/app/components/[slug]`
**Generated:** 2025-11-15T20:38:37.584932Z

---

## Overview

This directory (`apps/web/src/app/components/[slug]`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/components/[slug]



| File | Documentation | Keywords |
|------|---------------|----------|
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 121: apps/web/src/app/templates


**Folder Path:** `apps/web/src/app/templates`
**Generated:** 2025-11-15T20:38:37.586238Z

---

## Overview

This directory (`apps/web/src/app/templates`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/app/templates



| File | Documentation | Keywords |
|------|---------------|----------|
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 122: apps/web/src/components


**Folder Path:** `apps/web/src/components`
**Generated:** 2025-11-15T20:38:37.587703Z

---

## Overview

This directory (`apps/web/src/components`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 24
- **Keyword Files:** 24

### Subdirectories

- `icons/`
- `sections/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `anchor.tsx` | [View](anchor.tsx_docs.md) | [View](anchor.tsx_kw.md) |
| `button.tsx` | [View](button.tsx_docs.md) | [View](button.tsx_kw.md) |
| `code-block.tsx` | [View](code-block.tsx_docs.md) | [View](code-block.tsx_kw.md) |
| `code.tsx` | [View](code.tsx_docs.md) | [View](code.tsx_kw.md) |
| `component-code-view.tsx` | [View](component-code-view.tsx_docs.md) | [View](component-code-view.tsx_kw.md) |
| `component-preview.tsx` | [View](component-preview.tsx_docs.md) | [View](component-preview.tsx_kw.md) |
| `component-view.tsx` | [View](component-view.tsx_docs.md) | [View](component-view.tsx_kw.md) |
| `components-view.tsx` | [View](components-view.tsx_docs.md) | [View](components-view.tsx_kw.md) |
| `copy-code.tsx` | [View](copy-code.tsx_docs.md) | [View](copy-code.tsx_kw.md) |
| `footer.tsx` | [View](footer.tsx_docs.md) | [View](footer.tsx_kw.md) |
| `heading.tsx` | [View](heading.tsx_docs.md) | [View](heading.tsx_kw.md) |
| `icon-button.tsx` | [View](icon-button.tsx_docs.md) | [View](icon-button.tsx_kw.md) |
| `logo.tsx` | [View](logo.tsx_docs.md) | [View](logo.tsx_kw.md) |
| `menu.tsx` | [View](menu.tsx_docs.md) | [View](menu.tsx_kw.md) |
| `page-transition.tsx` | [View](page-transition.tsx_docs.md) | [View](page-transition.tsx_kw.md) |
| `page-wrapper.tsx` | [View](page-wrapper.tsx_docs.md) | [View](page-wrapper.tsx_kw.md) |
| `send.tsx` | [View](send.tsx_docs.md) | [View](send.tsx_kw.md) |
| `spotlight.tsx` | [View](spotlight.tsx_docs.md) | [View](spotlight.tsx_kw.md) |
| `tab-trigger.tsx` | [View](tab-trigger.tsx_docs.md) | [View](tab-trigger.tsx_kw.md) |
| `template.tsx` | [View](template.tsx_docs.md) | [View](template.tsx_kw.md) |
| `text.tsx` | [View](text.tsx_docs.md) | [View](text.tsx_kw.md) |
| `tooltip-content.tsx` | [View](tooltip-content.tsx_docs.md) | [View](tooltip-content.tsx_kw.md) |
| `tooltip.tsx` | [View](tooltip.tsx_docs.md) | [View](tooltip.tsx_kw.md) |
| `topbar.tsx` | [View](topbar.tsx_docs.md) | [View](topbar.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 123: apps/web/src/components/icons


**Folder Path:** `apps/web/src/components/icons`
**Generated:** 2025-11-15T20:38:37.597999Z

---

## Overview

This directory (`apps/web/src/components/icons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 6
- **Keyword Files:** 6

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/components/icons



| File | Documentation | Keywords |
|------|---------------|----------|
| `icon-arrow-left.tsx` | [View](icon-arrow-left.tsx_docs.md) | [View](icon-arrow-left.tsx_kw.md) |
| `icon-base.tsx` | [View](icon-base.tsx_docs.md) | [View](icon-base.tsx_kw.md) |
| `icon-file.tsx` | [View](icon-file.tsx_docs.md) | [View](icon-file.tsx_kw.md) |
| `icon-monitor.tsx` | [View](icon-monitor.tsx_docs.md) | [View](icon-monitor.tsx_kw.md) |
| `icon-phone.tsx` | [View](icon-phone.tsx_docs.md) | [View](icon-phone.tsx_kw.md) |
| `icon-source.tsx` | [View](icon-source.tsx_docs.md) | [View](icon-source.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 124: apps/web/src/components/sections


**Folder Path:** `apps/web/src/components/sections`
**Generated:** 2025-11-15T20:38:37.600606Z

---

## Overview

This directory (`apps/web/src/components/sections`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `playground/`
- `tools/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/components/sections



| File | Documentation | Keywords |
|------|---------------|----------|
| `hero.tsx` | [View](hero.tsx_docs.md) | [View](hero.tsx_kw.md) |
| `integration.tsx` | [View](integration.tsx_docs.md) | [View](integration.tsx_kw.md) |
| `patterns.tsx` | [View](patterns.tsx_docs.md) | [View](patterns.tsx_kw.md) |
| `primitives.tsx` | [View](primitives.tsx_docs.md) | [View](primitives.tsx_kw.md) |
| `testimonial.tsx` | [View](testimonial.tsx_docs.md) | [View](testimonial.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 125: apps/web/src/components/sections/playground


**Folder Path:** `apps/web/src/components/sections/playground`
**Generated:** 2025-11-15T20:38:37.604004Z

---

## Overview

This directory (`apps/web/src/components/sections/playground`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/components/sections/playground



| File | Documentation | Keywords |
|------|---------------|----------|
| `code-example.tsx` | [View](code-example.tsx_docs.md) | [View](code-example.tsx_kw.md) |
| `code-preview.tsx` | [View](code-preview.tsx_docs.md) | [View](code-preview.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |
| `utils.ts` | [View](utils.ts_docs.md) | [View](utils.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 126: apps/web/src/components/sections/tools


**Folder Path:** `apps/web/src/components/sections/tools`
**Generated:** 2025-11-15T20:38:37.607168Z

---

## Overview

This directory (`apps/web/src/components/sections/tools`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/components/sections/tools



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |
| `interactive-demo.tsx` | [View](interactive-demo.tsx_docs.md) | [View](interactive-demo.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 127: apps/web/src/hooks


**Folder Path:** `apps/web/src/hooks`
**Generated:** 2025-11-15T20:38:37.609786Z

---

## Overview

This directory (`apps/web/src/hooks`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/hooks



| File | Documentation | Keywords |
|------|---------------|----------|
| `use-stored-state.ts` | [View](use-stored-state.ts_docs.md) | [View](use-stored-state.ts_kw.md) |
| `useCollageTexture.ts` | [View](useCollageTexture.ts_docs.md) | [View](useCollageTexture.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 128: apps/web/src/illustrations


**Folder Path:** `apps/web/src/illustrations`
**Generated:** 2025-11-15T20:38:37.611377Z

---

## Overview

This directory (`apps/web/src/illustrations`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 25
- **Keyword Files:** 25

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/illustrations



| File | Documentation | Keywords |
|------|---------------|----------|
| `articles.tsx` | [View](articles.tsx_docs.md) | [View](articles.tsx_kw.md) |
| `avatars.tsx` | [View](avatars.tsx_docs.md) | [View](avatars.tsx_kw.md) |
| `buttons.tsx` | [View](buttons.tsx_docs.md) | [View](buttons.tsx_kw.md) |
| `code-block.tsx` | [View](code-block.tsx_docs.md) | [View](code-block.tsx_kw.md) |
| `code-inline.tsx` | [View](code-inline.tsx_docs.md) | [View](code-inline.tsx_kw.md) |
| `container.tsx` | [View](container.tsx_docs.md) | [View](container.tsx_kw.md) |
| `divider.tsx` | [View](divider.tsx_docs.md) | [View](divider.tsx_kw.md) |
| `ecommerce.tsx` | [View](ecommerce.tsx_docs.md) | [View](ecommerce.tsx_kw.md) |
| `features.tsx` | [View](features.tsx_docs.md) | [View](features.tsx_kw.md) |
| `feedback.tsx` | [View](feedback.tsx_docs.md) | [View](feedback.tsx_kw.md) |
| `footers.tsx` | [View](footers.tsx_docs.md) | [View](footers.tsx_kw.md) |
| `gallery.tsx` | [View](gallery.tsx_docs.md) | [View](gallery.tsx_kw.md) |
| `grid.tsx` | [View](grid.tsx_docs.md) | [View](grid.tsx_kw.md) |
| `headers.tsx` | [View](headers.tsx_docs.md) | [View](headers.tsx_kw.md) |
| `heading.tsx` | [View](heading.tsx_docs.md) | [View](heading.tsx_kw.md) |
| `image.tsx` | [View](image.tsx_docs.md) | [View](image.tsx_kw.md) |
| `link.tsx` | [View](link.tsx_docs.md) | [View](link.tsx_kw.md) |
| `list.tsx` | [View](list.tsx_docs.md) | [View](list.tsx_kw.md) |
| `markdown.tsx` | [View](markdown.tsx_docs.md) | [View](markdown.tsx_kw.md) |
| `marketing.tsx` | [View](marketing.tsx_docs.md) | [View](marketing.tsx_kw.md) |
| `pricing.tsx` | [View](pricing.tsx_docs.md) | [View](pricing.tsx_kw.md) |
| `section.tsx` | [View](section.tsx_docs.md) | [View](section.tsx_kw.md) |
| `stats.tsx` | [View](stats.tsx_docs.md) | [View](stats.tsx_kw.md) |
| `testimonials.tsx` | [View](testimonials.tsx_docs.md) | [View](testimonials.tsx_kw.md) |
| `text.tsx` | [View](text.tsx_docs.md) | [View](text.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 129: apps/web/src/styles


**Folder Path:** `apps/web/src/styles`
**Generated:** 2025-11-15T20:38:37.619451Z

---

## Overview

This directory (`apps/web/src/styles`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/styles



| File | Documentation | Keywords |
|------|---------------|----------|
| `globals.css` | [View](globals.css_docs.md) | [View](globals.css_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 130: apps/web/src/types


**Folder Path:** `apps/web/src/types`
**Generated:** 2025-11-15T20:38:37.620713Z

---

## Overview

This directory (`apps/web/src/types`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/types



| File | Documentation | Keywords |
|------|---------------|----------|
| `three.d.ts` | [View](three.d.ts_docs.md) | [View](three.d.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 131: apps/web/src/utils


**Folder Path:** `apps/web/src/utils`
**Generated:** 2025-11-15T20:38:37.622007Z

---

## Overview

This directory (`apps/web/src/utils`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 6
- **Keyword Files:** 6

### Subdirectories

- `spam-assassin/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `as.ts` | [View](as.ts_docs.md) | [View](as.ts_kw.md) |
| `convert-uris-into-urls.spec.ts` | [View](convert-uris-into-urls.spec.ts_docs.md) | [View](convert-uris-into-urls.spec.ts_kw.md) |
| `convert-uris-into-urls.ts` | [View](convert-uris-into-urls.ts_docs.md) | [View](convert-uris-into-urls.ts_kw.md) |
| `slugify.ts` | [View](slugify.ts_docs.md) | [View](slugify.ts_kw.md) |
| `unreachable.ts` | [View](unreachable.ts_docs.md) | [View](unreachable.ts_kw.md) |
| `use-scroll.tsx` | [View](use-scroll.tsx_docs.md) | [View](use-scroll.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 132: apps/web/src/utils/spam-assassin


**Folder Path:** `apps/web/src/utils/spam-assassin`
**Generated:** 2025-11-15T20:38:37.624447Z

---

## Overview

This directory (`apps/web/src/utils/spam-assassin`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/utils/spam-assassin



| File | Documentation | Keywords |
|------|---------------|----------|
| `parse-pointing-table-rows.spec.ts` | [View](parse-pointing-table-rows.spec.ts_docs.md) | [View](parse-pointing-table-rows.spec.ts_kw.md) |
| `parse-pointing-table-rows.ts` | [View](parse-pointing-table-rows.ts_docs.md) | [View](parse-pointing-table-rows.ts_kw.md) |
| `send-to-spamd.ts` | [View](send-to-spamd.ts_docs.md) | [View](send-to-spamd.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 133: apps/web/src/utils/spam-assassin/__snapshots__


**Folder Path:** `apps/web/src/utils/spam-assassin/__snapshots__`
**Generated:** 2025-11-15T20:38:37.627394Z

---

## Overview

This directory (`apps/web/src/utils/spam-assassin/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/utils/spam-assassin/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `parse-pointing-table-rows.spec.ts.snap` | [View](parse-pointing-table-rows.spec.ts.snap_docs.md) | [View](parse-pointing-table-rows.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 134: apps/web/src/webgl


**Folder Path:** `apps/web/src/webgl`
**Generated:** 2025-11-15T20:38:37.628878Z

---

## Overview

This directory (`apps/web/src/webgl`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `materials/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/webgl



| File | Documentation | Keywords |
|------|---------------|----------|
| `Billboard.tsx` | [View](Billboard.tsx_docs.md) | [View](Billboard.tsx_kw.md) |
| `View.tsx` | [View](View.tsx_docs.md) | [View](View.tsx_kw.md) |
| `getCanvasTexture.js` | [View](getCanvasTexture.js_docs.md) | [View](getCanvasTexture.js_kw.md) |
| `tower.tsx` | [View](tower.tsx_docs.md) | [View](tower.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 135: apps/web/src/webgl/materials


**Folder Path:** `apps/web/src/webgl/materials`
**Generated:** 2025-11-15T20:38:37.631194Z

---

## Overview

This directory (`apps/web/src/webgl/materials`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in apps/web/src/webgl/materials



| File | Documentation | Keywords |
|------|---------------|----------|
| `MeshBannerMaterial.ts` | [View](MeshBannerMaterial.ts_docs.md) | [View](MeshBannerMaterial.ts_kw.md) |
| `MeshImageMaterial.ts` | [View](MeshImageMaterial.ts_docs.md) | [View](MeshImageMaterial.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 136: benchmarks


**Folder Path:** `benchmarks`
**Generated:** 2025-11-15T20:38:37.632642Z

---

## Overview

This directory (`benchmarks`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `preview-server/`
- `tailwind-component/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks

---

# Chapter 137: benchmarks/preview-server


**Folder Path:** `benchmarks/preview-server`
**Generated:** 2025-11-15T20:38:37.633417Z

---

## Overview

This directory (`benchmarks/preview-server`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/preview-server



| File | Documentation | Keywords |
|------|---------------|----------|
| `bench-results-30-iterations.json` | [View](bench-results-30-iterations.json_docs.md) | [View](bench-results-30-iterations.json_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `startup-bench-results-30-iterations.json` | [View](startup-bench-results-30-iterations.json_docs.md) | [View](startup-bench-results-30-iterations.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 138: benchmarks/preview-server/src


**Folder Path:** `benchmarks/preview-server/src`
**Generated:** 2025-11-15T20:38:37.635033Z

---

## Overview

This directory (`benchmarks/preview-server/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/preview-server/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `local-vs-2.1.7-canary.2-on-startup.ts` | [View](local-vs-2.1.7-canary.2-on-startup.ts_docs.md) | [View](local-vs-2.1.7-canary.2-on-startup.ts_kw.md) |
| `local-vs-2.1.7-canary.2.ts` | [View](local-vs-2.1.7-canary.2.ts_docs.md) | [View](local-vs-2.1.7-canary.2.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 139: benchmarks/preview-server/src/utils


**Folder Path:** `benchmarks/preview-server/src/utils`
**Generated:** 2025-11-15T20:38:37.636432Z

---

## Overview

This directory (`benchmarks/preview-server/src/utils`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/preview-server/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `run-server-and-fetch-preview-page.ts` | [View](run-server-and-fetch-preview-page.ts_docs.md) | [View](run-server-and-fetch-preview-page.ts_kw.md) |
| `run-server.ts` | [View](run-server.ts_docs.md) | [View](run-server.ts_kw.md) |
| `sleep.ts` | [View](sleep.ts_docs.md) | [View](sleep.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 140: benchmarks/tailwind-component


**Folder Path:** `benchmarks/tailwind-component`
**Generated:** 2025-11-15T20:38:37.638196Z

---

## Overview

This directory (`benchmarks/tailwind-component`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 6
- **Keyword Files:** 6

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/tailwind-component



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `bench-results-100-iterations.json` | [View](bench-results-100-iterations.json_docs.md) | [View](bench-results-100-iterations.json_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tailwind.config.js` | [View](tailwind.config.js_docs.md) | [View](tailwind.config.js_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 141: benchmarks/tailwind-component/src


**Folder Path:** `benchmarks/tailwind-component/src`
**Generated:** 2025-11-15T20:38:37.640461Z

---

## Overview

This directory (`benchmarks/tailwind-component/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/tailwind-component/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `benchmark-0.0.12-vs-local-version.tsx` | [View](benchmark-0.0.12-vs-local-version.tsx_docs.md) | [View](benchmark-0.0.12-vs-local-version.tsx_kw.md) |
| `benchmark-0.0.17-vs-local-version.tsx` | [View](benchmark-0.0.17-vs-local-version.tsx_docs.md) | [View](benchmark-0.0.17-vs-local-version.tsx_kw.md) |
| `benchmark-with-vs-without.tsx` | [View](benchmark-with-vs-without.tsx_docs.md) | [View](benchmark-with-vs-without.tsx_kw.md) |
| `tailwind-render.tsx` | [View](tailwind-render.tsx_docs.md) | [View](tailwind-render.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 142: benchmarks/tailwind-component/src/emails


**Folder Path:** `benchmarks/tailwind-component/src/emails`
**Generated:** 2025-11-15T20:38:37.642141Z

---

## Overview

This directory (`benchmarks/tailwind-component/src/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in benchmarks/tailwind-component/src/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `with-tailwind.tsx` | [View](with-tailwind.tsx_docs.md) | [View](with-tailwind.tsx_kw.md) |
| `without-tailwind.tsx` | [View](without-tailwind.tsx_docs.md) | [View](without-tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 143: examples


**Folder Path:** `examples`
**Generated:** 2025-11-15T20:38:37.644182Z

---

## Overview

This directory (`examples`) contains 

## Structure

- **Subdirectories:** 8
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `aws-ses/`
- `mailersend/`
- `nodemailer/`
- `plunk/`
- `postmark/`
- `resend/`
- `scaleway/`
- `sendgrid/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples

---

# Chapter 144: examples/aws-ses


**Folder Path:** `examples/aws-ses`
**Generated:** 2025-11-15T20:38:37.644920Z

---

## Overview

This directory (`examples/aws-ses`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/aws-ses



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 145: examples/aws-ses/src


**Folder Path:** `examples/aws-ses/src`
**Generated:** 2025-11-15T20:38:37.646294Z

---

## Overview

This directory (`examples/aws-ses/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/aws-ses/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 146: examples/mailersend


**Folder Path:** `examples/mailersend`
**Generated:** 2025-11-15T20:38:37.647667Z

---

## Overview

This directory (`examples/mailersend`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/mailersend



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 147: examples/mailersend/src


**Folder Path:** `examples/mailersend/src`
**Generated:** 2025-11-15T20:38:37.648957Z

---

## Overview

This directory (`examples/mailersend/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/mailersend/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 148: examples/nodemailer


**Folder Path:** `examples/nodemailer`
**Generated:** 2025-11-15T20:38:37.650313Z

---

## Overview

This directory (`examples/nodemailer`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/nodemailer



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 149: examples/nodemailer/src


**Folder Path:** `examples/nodemailer/src`
**Generated:** 2025-11-15T20:38:37.651685Z

---

## Overview

This directory (`examples/nodemailer/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/nodemailer/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 150: examples/plunk


**Folder Path:** `examples/plunk`
**Generated:** 2025-11-15T20:38:37.653015Z

---

## Overview

This directory (`examples/plunk`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/plunk



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 151: examples/plunk/src


**Folder Path:** `examples/plunk/src`
**Generated:** 2025-11-15T20:38:37.654180Z

---

## Overview

This directory (`examples/plunk/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/plunk/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 152: examples/postmark


**Folder Path:** `examples/postmark`
**Generated:** 2025-11-15T20:38:37.655408Z

---

## Overview

This directory (`examples/postmark`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/postmark



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 153: examples/postmark/src


**Folder Path:** `examples/postmark/src`
**Generated:** 2025-11-15T20:38:37.656766Z

---

## Overview

This directory (`examples/postmark/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/postmark/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 154: examples/resend


**Folder Path:** `examples/resend`
**Generated:** 2025-11-15T20:38:37.657955Z

---

## Overview

This directory (`examples/resend`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `src/`
- `transactional/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend



| File | Documentation | Keywords |
|------|---------------|----------|
| `next-env.d.ts` | [View](next-env.d.ts_docs.md) | [View](next-env.d.ts_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 155: examples/resend/src


**Folder Path:** `examples/resend/src`
**Generated:** 2025-11-15T20:38:37.659432Z

---

## Overview

This directory (`examples/resend/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `lib/`
- `pages/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/src

---

# Chapter 156: examples/resend/src/lib


**Folder Path:** `examples/resend/src/lib`
**Generated:** 2025-11-15T20:38:37.660179Z

---

## Overview

This directory (`examples/resend/src/lib`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/src/lib



| File | Documentation | Keywords |
|------|---------------|----------|
| `resend.ts` | [View](resend.ts_docs.md) | [View](resend.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 157: examples/resend/src/pages


**Folder Path:** `examples/resend/src/pages`
**Generated:** 2025-11-15T20:38:37.661126Z

---

## Overview

This directory (`examples/resend/src/pages`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `api/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/src/pages

---

# Chapter 158: examples/resend/src/pages/api


**Folder Path:** `examples/resend/src/pages/api`
**Generated:** 2025-11-15T20:38:37.661896Z

---

## Overview

This directory (`examples/resend/src/pages/api`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/src/pages/api



| File | Documentation | Keywords |
|------|---------------|----------|
| `send.ts` | [View](send.ts_docs.md) | [View](send.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 159: examples/resend/transactional


**Folder Path:** `examples/resend/transactional`
**Generated:** 2025-11-15T20:38:37.663091Z

---

## Overview

This directory (`examples/resend/transactional`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/transactional

---

# Chapter 160: examples/resend/transactional/emails


**Folder Path:** `examples/resend/transactional/emails`
**Generated:** 2025-11-15T20:38:37.663799Z

---

## Overview

This directory (`examples/resend/transactional/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/resend/transactional/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `waitlist.tsx` | [View](waitlist.tsx_docs.md) | [View](waitlist.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 161: examples/scaleway


**Folder Path:** `examples/scaleway`
**Generated:** 2025-11-15T20:38:37.665061Z

---

## Overview

This directory (`examples/scaleway`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `next/`
- `node/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway

---

# Chapter 162: examples/scaleway/next


**Folder Path:** `examples/scaleway/next`
**Generated:** 2025-11-15T20:38:37.665759Z

---

## Overview

This directory (`examples/scaleway/next`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `src/`
- `transactional/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next



| File | Documentation | Keywords |
|------|---------------|----------|
| `next-env.d.ts` | [View](next-env.d.ts_docs.md) | [View](next-env.d.ts_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 163: examples/scaleway/next/src


**Folder Path:** `examples/scaleway/next/src`
**Generated:** 2025-11-15T20:38:37.667464Z

---

## Overview

This directory (`examples/scaleway/next/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `lib/`
- `pages/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/src

---

# Chapter 164: examples/scaleway/next/src/lib


**Folder Path:** `examples/scaleway/next/src/lib`
**Generated:** 2025-11-15T20:38:37.668471Z

---

## Overview

This directory (`examples/scaleway/next/src/lib`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/src/lib



| File | Documentation | Keywords |
|------|---------------|----------|
| `scaleway.ts` | [View](scaleway.ts_docs.md) | [View](scaleway.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 165: examples/scaleway/next/src/pages


**Folder Path:** `examples/scaleway/next/src/pages`
**Generated:** 2025-11-15T20:38:37.670074Z

---

## Overview

This directory (`examples/scaleway/next/src/pages`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `api/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/src/pages

---

# Chapter 166: examples/scaleway/next/src/pages/api


**Folder Path:** `examples/scaleway/next/src/pages/api`
**Generated:** 2025-11-15T20:38:37.671059Z

---

## Overview

This directory (`examples/scaleway/next/src/pages/api`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/src/pages/api



| File | Documentation | Keywords |
|------|---------------|----------|
| `send.tsx` | [View](send.tsx_docs.md) | [View](send.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 167: examples/scaleway/next/transactional


**Folder Path:** `examples/scaleway/next/transactional`
**Generated:** 2025-11-15T20:38:37.672468Z

---

## Overview

This directory (`examples/scaleway/next/transactional`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/transactional

---

# Chapter 168: examples/scaleway/next/transactional/emails


**Folder Path:** `examples/scaleway/next/transactional/emails`
**Generated:** 2025-11-15T20:38:37.673318Z

---

## Overview

This directory (`examples/scaleway/next/transactional/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/next/transactional/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `waitlist.tsx` | [View](waitlist.tsx_docs.md) | [View](waitlist.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 169: examples/scaleway/node


**Folder Path:** `examples/scaleway/node`
**Generated:** 2025-11-15T20:38:37.674492Z

---

## Overview

This directory (`examples/scaleway/node`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/node



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 170: examples/scaleway/node/src


**Folder Path:** `examples/scaleway/node/src`
**Generated:** 2025-11-15T20:38:37.675809Z

---

## Overview

This directory (`examples/scaleway/node/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/scaleway/node/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 171: examples/sendgrid


**Folder Path:** `examples/sendgrid`
**Generated:** 2025-11-15T20:38:37.677362Z

---

## Overview

This directory (`examples/sendgrid`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains example code and demonstrations.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/sendgrid



| File | Documentation | Keywords |
|------|---------------|----------|
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 172: examples/sendgrid/src


**Folder Path:** `examples/sendgrid/src`
**Generated:** 2025-11-15T20:38:37.678723Z

---

## Overview

This directory (`examples/sendgrid/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in examples/sendgrid/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `email.tsx` | [View](email.tsx_docs.md) | [View](email.tsx_kw.md) |
| `index.tsx` | [View](index.tsx_docs.md) | [View](index.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 173: packages


**Folder Path:** `packages`
**Generated:** 2025-11-15T20:38:37.679980Z

---

## Overview

This directory (`packages`) contains React components. 

## Structure

- **Subdirectories:** 25
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `body/`
- `button/`
- `code-block/`
- `code-inline/`
- `column/`
- `components/`
- `container/`
- `create-email/`
- `font/`
- `head/`
- `heading/`
- `hr/`
- `html/`
- `img/`
- `link/`
- `markdown/`
- `preview/`
- `preview-server/`
- `react-email/`
- `render/`
- `row/`
- `section/`
- `tailwind/`
- `text/`
- `tsconfig/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages

---

# Chapter 174: packages/body


**Folder Path:** `packages/body`
**Generated:** 2025-11-15T20:38:37.680732Z

---

## Overview

This directory (`packages/body`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/body



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 175: packages/body/src


**Folder Path:** `packages/body/src`
**Generated:** 2025-11-15T20:38:37.683100Z

---

## Overview

This directory (`packages/body/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/body/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `body.spec.tsx` | [View](body.spec.tsx_docs.md) | [View](body.spec.tsx_kw.md) |
| `body.tsx` | [View](body.tsx_docs.md) | [View](body.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `margin-properties.ts` | [View](margin-properties.ts_docs.md) | [View](margin-properties.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 176: packages/body/src/__snapshots__


**Folder Path:** `packages/body/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.685342Z

---

## Overview

This directory (`packages/body/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/body/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `body.spec.tsx.snap` | [View](body.spec.tsx.snap_docs.md) | [View](body.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 177: packages/button


**Folder Path:** `packages/button`
**Generated:** 2025-11-15T20:38:37.686867Z

---

## Overview

This directory (`packages/button`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/button



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 178: packages/button/src


**Folder Path:** `packages/button/src`
**Generated:** 2025-11-15T20:38:37.689732Z

---

## Overview

This directory (`packages/button/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/button/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `button.spec.tsx` | [View](button.spec.tsx_docs.md) | [View](button.spec.tsx_kw.md) |
| `button.tsx` | [View](button.tsx_docs.md) | [View](button.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 179: packages/button/src/__snapshots__


**Folder Path:** `packages/button/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.691895Z

---

## Overview

This directory (`packages/button/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/button/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `button.spec.tsx.snap` | [View](button.spec.tsx.snap_docs.md) | [View](button.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 180: packages/button/src/utils


**Folder Path:** `packages/button/src/utils`
**Generated:** 2025-11-15T20:38:37.693192Z

---

## Overview

This directory (`packages/button/src/utils`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/button/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `parse-padding.ts` | [View](parse-padding.ts_docs.md) | [View](parse-padding.ts_kw.md) |
| `px-to-pt.ts` | [View](px-to-pt.ts_docs.md) | [View](px-to-pt.ts_kw.md) |
| `utils.spec.ts` | [View](utils.spec.ts_docs.md) | [View](utils.spec.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 181: packages/code-block


**Folder Path:** `packages/code-block`
**Generated:** 2025-11-15T20:38:37.695061Z

---

## Overview

This directory (`packages/code-block`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/code-block



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 182: packages/code-block/src


**Folder Path:** `packages/code-block/src`
**Generated:** 2025-11-15T20:38:37.698044Z

---

## Overview

This directory (`packages/code-block/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/code-block/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `code-block.tsx` | [View](code-block.tsx_docs.md) | [View](code-block.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `languages-available.ts` | [View](languages-available.ts_docs.md) | [View](languages-available.ts_kw.md) |
| `prism.ts` | [View](prism.ts_docs.md) | [View](prism.ts_kw.md) |
| `themes.ts` | [View](themes.ts_docs.md) | [View](themes.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 183: packages/code-inline


**Folder Path:** `packages/code-inline`
**Generated:** 2025-11-15T20:38:37.746920Z

---

## Overview

This directory (`packages/code-inline`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/code-inline



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 184: packages/code-inline/src


**Folder Path:** `packages/code-inline/src`
**Generated:** 2025-11-15T20:38:37.749606Z

---

## Overview

This directory (`packages/code-inline/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/code-inline/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `code-inline.tsx` | [View](code-inline.tsx_docs.md) | [View](code-inline.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 185: packages/column


**Folder Path:** `packages/column`
**Generated:** 2025-11-15T20:38:37.751125Z

---

## Overview

This directory (`packages/column`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/column



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 186: packages/column/src


**Folder Path:** `packages/column/src`
**Generated:** 2025-11-15T20:38:37.753591Z

---

## Overview

This directory (`packages/column/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/column/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `column.spec.tsx` | [View](column.spec.tsx_docs.md) | [View](column.spec.tsx_kw.md) |
| `column.tsx` | [View](column.tsx_docs.md) | [View](column.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 187: packages/column/src/__snapshots__


**Folder Path:** `packages/column/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.755361Z

---

## Overview

This directory (`packages/column/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/column/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `column.spec.tsx.snap` | [View](column.spec.tsx.snap_docs.md) | [View](column.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 188: packages/components


**Folder Path:** `packages/components`
**Generated:** 2025-11-15T20:38:37.756389Z

---

## Overview

This directory (`packages/components`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains reusable component definitions.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 189: packages/components/src


**Folder Path:** `packages/components/src`
**Generated:** 2025-11-15T20:38:37.758805Z

---

## Overview

This directory (`packages/components/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/components/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 190: packages/components/src/__snapshots__


**Folder Path:** `packages/components/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.759817Z

---

## Overview

This directory (`packages/components/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/components/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `heading.spec.tsx.snap` | [View](heading.spec.tsx.snap_docs.md) | [View](heading.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 191: packages/container


**Folder Path:** `packages/container`
**Generated:** 2025-11-15T20:38:37.760784Z

---

## Overview

This directory (`packages/container`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/container



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 192: packages/container/src


**Folder Path:** `packages/container/src`
**Generated:** 2025-11-15T20:38:37.762764Z

---

## Overview

This directory (`packages/container/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/container/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `container.spec.tsx` | [View](container.spec.tsx_docs.md) | [View](container.spec.tsx_kw.md) |
| `container.tsx` | [View](container.tsx_docs.md) | [View](container.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 193: packages/container/src/__snapshots__


**Folder Path:** `packages/container/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.764443Z

---

## Overview

This directory (`packages/container/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/container/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `container.spec.tsx.snap` | [View](container.spec.tsx.snap_docs.md) | [View](container.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 194: packages/create-email


**Folder Path:** `packages/create-email`
**Generated:** 2025-11-15T20:38:37.765606Z

---

## Overview

This directory (`packages/create-email`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 8
- **Keyword Files:** 8

### Subdirectories

- `src/`
- `template/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/create-email



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `.npmignore` | [View](.npmignore_docs.md) | [View](.npmignore_kw.md) |
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 195: packages/create-email/src


**Folder Path:** `packages/create-email/src`
**Generated:** 2025-11-15T20:38:37.768753Z

---

## Overview

This directory (`packages/create-email/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/create-email/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.js` | [View](index.js_docs.md) | [View](index.js_kw.md) |
| `index.spec.ts` | [View](index.spec.ts_docs.md) | [View](index.spec.ts_kw.md) |
| `tree.js` | [View](tree.js_docs.md) | [View](tree.js_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 196: packages/create-email/template


**Folder Path:** `packages/create-email/template`
**Generated:** 2025-11-15T20:38:37.770580Z

---

## Overview

This directory (`packages/create-email/template`) contains a Node.js package. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/create-email/template



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 197: packages/create-email/template/emails


**Folder Path:** `packages/create-email/template/emails`
**Generated:** 2025-11-15T20:38:37.772629Z

---

## Overview

This directory (`packages/create-email/template/emails`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `static/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/create-email/template/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `notion-magic-link.tsx` | [View](notion-magic-link.tsx_docs.md) | [View](notion-magic-link.tsx_kw.md) |
| `plaid-verify-identity.tsx` | [View](plaid-verify-identity.tsx_docs.md) | [View](plaid-verify-identity.tsx_kw.md) |
| `stripe-welcome.tsx` | [View](stripe-welcome.tsx_docs.md) | [View](stripe-welcome.tsx_kw.md) |
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 198: packages/create-email/template/emails/static


**Folder Path:** `packages/create-email/template/emails/static`
**Generated:** 2025-11-15T20:38:37.775721Z

---

## Overview

This directory (`packages/create-email/template/emails/static`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 8
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/create-email/template/emails/static



| File | Documentation | Keywords |
|------|---------------|----------|
| `notion-logo.png` | [View](notion-logo.png_docs.md) | - |
| `plaid-logo.png` | [View](plaid-logo.png_docs.md) | - |
| `plaid.png` | [View](plaid.png_docs.md) | - |
| `stripe-logo.png` | [View](stripe-logo.png_docs.md) | - |
| `vercel-arrow.png` | [View](vercel-arrow.png_docs.md) | - |
| `vercel-logo.png` | [View](vercel-logo.png_docs.md) | - |
| `vercel-team.png` | [View](vercel-team.png_docs.md) | - |
| `vercel-user.png` | [View](vercel-user.png_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 199: packages/font


**Folder Path:** `packages/font`
**Generated:** 2025-11-15T20:38:37.776572Z

---

## Overview

This directory (`packages/font`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/font



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 200: packages/font/src


**Folder Path:** `packages/font/src`
**Generated:** 2025-11-15T20:38:37.778647Z

---

## Overview

This directory (`packages/font/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/font/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `font.spec.tsx` | [View](font.spec.tsx_docs.md) | [View](font.spec.tsx_kw.md) |
| `font.tsx` | [View](font.tsx_docs.md) | [View](font.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 201: packages/font/src/__snapshots__


**Folder Path:** `packages/font/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.780485Z

---

## Overview

This directory (`packages/font/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/font/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `font.spec.tsx.snap` | [View](font.spec.tsx.snap_docs.md) | [View](font.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 202: packages/head


**Folder Path:** `packages/head`
**Generated:** 2025-11-15T20:38:37.781726Z

---

## Overview

This directory (`packages/head`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/head



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 203: packages/head/src


**Folder Path:** `packages/head/src`
**Generated:** 2025-11-15T20:38:37.783770Z

---

## Overview

This directory (`packages/head/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/head/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `head.spec.tsx` | [View](head.spec.tsx_docs.md) | [View](head.spec.tsx_kw.md) |
| `head.tsx` | [View](head.tsx_docs.md) | [View](head.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 204: packages/head/src/__snapshots__


**Folder Path:** `packages/head/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.785171Z

---

## Overview

This directory (`packages/head/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/head/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `head.spec.tsx.snap` | [View](head.spec.tsx.snap_docs.md) | [View](head.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 205: packages/heading


**Folder Path:** `packages/heading`
**Generated:** 2025-11-15T20:38:37.786141Z

---

## Overview

This directory (`packages/heading`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/heading



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 206: packages/heading/src


**Folder Path:** `packages/heading/src`
**Generated:** 2025-11-15T20:38:37.788243Z

---

## Overview

This directory (`packages/heading/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/heading/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `heading.spec.tsx` | [View](heading.spec.tsx_docs.md) | [View](heading.spec.tsx_kw.md) |
| `heading.tsx` | [View](heading.tsx_docs.md) | [View](heading.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 207: packages/heading/src/__snapshots__


**Folder Path:** `packages/heading/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.789835Z

---

## Overview

This directory (`packages/heading/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/heading/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `heading.spec.tsx.snap` | [View](heading.spec.tsx.snap_docs.md) | [View](heading.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 208: packages/heading/src/utils


**Folder Path:** `packages/heading/src/utils`
**Generated:** 2025-11-15T20:38:37.790816Z

---

## Overview

This directory (`packages/heading/src/utils`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/heading/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `as.ts` | [View](as.ts_docs.md) | [View](as.ts_kw.md) |
| `spaces.ts` | [View](spaces.ts_docs.md) | [View](spaces.ts_kw.md) |
| `utils.spec.ts` | [View](utils.spec.ts_docs.md) | [View](utils.spec.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 209: packages/hr


**Folder Path:** `packages/hr`
**Generated:** 2025-11-15T20:38:37.792293Z

---

## Overview

This directory (`packages/hr`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/hr



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 210: packages/hr/src


**Folder Path:** `packages/hr/src`
**Generated:** 2025-11-15T20:38:37.794254Z

---

## Overview

This directory (`packages/hr/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/hr/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `hr.spec.tsx` | [View](hr.spec.tsx_docs.md) | [View](hr.spec.tsx_kw.md) |
| `hr.tsx` | [View](hr.tsx_docs.md) | [View](hr.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 211: packages/hr/src/__snapshots__


**Folder Path:** `packages/hr/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.795732Z

---

## Overview

This directory (`packages/hr/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/hr/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `hr.spec.tsx.snap` | [View](hr.spec.tsx.snap_docs.md) | [View](hr.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 212: packages/html


**Folder Path:** `packages/html`
**Generated:** 2025-11-15T20:38:37.796750Z

---

## Overview

This directory (`packages/html`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/html



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 213: packages/html/src


**Folder Path:** `packages/html/src`
**Generated:** 2025-11-15T20:38:37.798843Z

---

## Overview

This directory (`packages/html/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/html/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `html.spec.tsx` | [View](html.spec.tsx_docs.md) | [View](html.spec.tsx_kw.md) |
| `html.tsx` | [View](html.tsx_docs.md) | [View](html.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 214: packages/html/src/__snapshots__


**Folder Path:** `packages/html/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.800158Z

---

## Overview

This directory (`packages/html/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/html/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `html.spec.tsx.snap` | [View](html.spec.tsx.snap_docs.md) | [View](html.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 215: packages/img


**Folder Path:** `packages/img`
**Generated:** 2025-11-15T20:38:37.801110Z

---

## Overview

This directory (`packages/img`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/img



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 216: packages/img/src


**Folder Path:** `packages/img/src`
**Generated:** 2025-11-15T20:38:37.803189Z

---

## Overview

This directory (`packages/img/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/img/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `img.spec.tsx` | [View](img.spec.tsx_docs.md) | [View](img.spec.tsx_kw.md) |
| `img.tsx` | [View](img.tsx_docs.md) | [View](img.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 217: packages/img/src/__snapshots__


**Folder Path:** `packages/img/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.804570Z

---

## Overview

This directory (`packages/img/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/img/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `img.spec.tsx.snap` | [View](img.spec.tsx.snap_docs.md) | [View](img.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 218: packages/link


**Folder Path:** `packages/link`
**Generated:** 2025-11-15T20:38:37.805759Z

---

## Overview

This directory (`packages/link`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/link



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 219: packages/link/src


**Folder Path:** `packages/link/src`
**Generated:** 2025-11-15T20:38:37.808251Z

---

## Overview

This directory (`packages/link/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/link/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `link.spec.tsx` | [View](link.spec.tsx_docs.md) | [View](link.spec.tsx_kw.md) |
| `link.tsx` | [View](link.tsx_docs.md) | [View](link.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 220: packages/link/src/__snapshots__


**Folder Path:** `packages/link/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.809663Z

---

## Overview

This directory (`packages/link/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/link/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `link.spec.tsx.snap` | [View](link.spec.tsx.snap_docs.md) | [View](link.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 221: packages/markdown


**Folder Path:** `packages/markdown`
**Generated:** 2025-11-15T20:38:37.810719Z

---

## Overview

This directory (`packages/markdown`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/markdown



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 222: packages/markdown/src


**Folder Path:** `packages/markdown/src`
**Generated:** 2025-11-15T20:38:37.812998Z

---

## Overview

This directory (`packages/markdown/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `__snapshots__/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/markdown/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `markdown.spec.tsx` | [View](markdown.spec.tsx_docs.md) | [View](markdown.spec.tsx_kw.md) |
| `markdown.tsx` | [View](markdown.tsx_docs.md) | [View](markdown.tsx_kw.md) |
| `styles.ts` | [View](styles.ts_docs.md) | [View](styles.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 223: packages/markdown/src/__snapshots__


**Folder Path:** `packages/markdown/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.815160Z

---

## Overview

This directory (`packages/markdown/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/markdown/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `markdown.spec.tsx.snap` | [View](markdown.spec.tsx.snap_docs.md) | [View](markdown.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 224: packages/markdown/src/utils


**Folder Path:** `packages/markdown/src/utils`
**Generated:** 2025-11-15T20:38:37.816324Z

---

## Overview

This directory (`packages/markdown/src/utils`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/markdown/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `parse-css-in-js-to-inline-css.ts` | [View](parse-css-in-js-to-inline-css.ts_docs.md) | [View](parse-css-in-js-to-inline-css.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 225: packages/preview


**Folder Path:** `packages/preview`
**Generated:** 2025-11-15T20:38:37.817378Z

---

## Overview

This directory (`packages/preview`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 226: packages/preview-server


**Folder Path:** `packages/preview-server`
**Generated:** 2025-11-15T20:38:37.819515Z

---

## Overview

This directory (`packages/preview-server`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 4
- **Documentation Files:** 13
- **Keyword Files:** 13

### Subdirectories

- `emails/`
- `jsx-runtime/`
- `scripts/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `.npmignore` | [View](.npmignore_docs.md) | [View](.npmignore_kw.md) |
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `index.mjs` | [View](index.mjs_docs.md) | [View](index.mjs_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `module-punycode.d.ts` | [View](module-punycode.d.ts_docs.md) | [View](module-punycode.d.ts_kw.md) |
| `next.config.mjs` | [View](next.config.mjs_docs.md) | [View](next.config.mjs_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `postcss.config.js` | [View](postcss.config.js_docs.md) | [View](postcss.config.js_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tailwind.config.ts` | [View](tailwind.config.ts_docs.md) | [View](tailwind.config.ts_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 227: packages/preview-server/emails


**Folder Path:** `packages/preview-server/emails`
**Generated:** 2025-11-15T20:38:37.824331Z

---

## Overview

This directory (`packages/preview-server/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitkeep` | [View](.gitkeep_docs.md) | [View](.gitkeep_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 228: packages/preview-server/jsx-runtime


**Folder Path:** `packages/preview-server/jsx-runtime`
**Generated:** 2025-11-15T20:38:37.825127Z

---

## Overview

This directory (`packages/preview-server/jsx-runtime`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/jsx-runtime



| File | Documentation | Keywords |
|------|---------------|----------|
| `jsx-dev-runtime.js` | [View](jsx-dev-runtime.js_docs.md) | [View](jsx-dev-runtime.js_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 229: packages/preview-server/scripts


**Folder Path:** `packages/preview-server/scripts`
**Generated:** 2025-11-15T20:38:37.826286Z

---

## Overview

This directory (`packages/preview-server/scripts`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains build scripts and automation tools.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts



| File | Documentation | Keywords |
|------|---------------|----------|
| `build-preview-server.mts` | [View](build-preview-server.mts_docs.md) | [View](build-preview-server.mts_kw.md) |
| `dev.mts` | [View](dev.mts_docs.md) | [View](dev.mts_kw.md) |
| `fill-caniemail-data.mts` | [View](fill-caniemail-data.mts_docs.md) | [View](fill-caniemail-data.mts_kw.md) |
| `seed.mts` | [View](seed.mts_docs.md) | [View](seed.mts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 230: packages/preview-server/scripts/utils


**Folder Path:** `packages/preview-server/scripts/utils`
**Generated:** 2025-11-15T20:38:37.828192Z

---

## Overview

This directory (`packages/preview-server/scripts/utils`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `default-seed/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains utility functions and helper modules.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts/utils

---

# Chapter 231: packages/preview-server/scripts/utils/default-seed


**Folder Path:** `packages/preview-server/scripts/utils/default-seed`
**Generated:** 2025-11-15T20:38:37.828909Z

---

## Overview

This directory (`packages/preview-server/scripts/utils/default-seed`) contains 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `auth/`
- `communications/`
- `marketing/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains utility functions and helper modules.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts/utils/default-seed



| File | Documentation | Keywords |
|------|---------------|----------|
| `feedback-request.tsx` | [View](feedback-request.tsx_docs.md) | [View](feedback-request.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 232: packages/preview-server/scripts/utils/default-seed/auth


**Folder Path:** `packages/preview-server/scripts/utils/default-seed/auth`
**Generated:** 2025-11-15T20:38:37.830089Z

---

## Overview

This directory (`packages/preview-server/scripts/utils/default-seed/auth`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains utility functions and helper modules.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts/utils/default-seed/auth



| File | Documentation | Keywords |
|------|---------------|----------|
| `account-confirmation.tsx` | [View](account-confirmation.tsx_docs.md) | [View](account-confirmation.tsx_kw.md) |
| `forgot-password.tsx` | [View](forgot-password.tsx_docs.md) | [View](forgot-password.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 233: packages/preview-server/scripts/utils/default-seed/communications


**Folder Path:** `packages/preview-server/scripts/utils/default-seed/communications`
**Generated:** 2025-11-15T20:38:37.831860Z

---

## Overview

This directory (`packages/preview-server/scripts/utils/default-seed/communications`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains utility functions and helper modules.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts/utils/default-seed/communications



| File | Documentation | Keywords |
|------|---------------|----------|
| `payment-overdue.tsx` | [View](payment-overdue.tsx_docs.md) | [View](payment-overdue.tsx_kw.md) |
| `team-invite.tsx` | [View](team-invite.tsx_docs.md) | [View](team-invite.tsx_kw.md) |
| `webhooks-failed.tsx` | [View](webhooks-failed.tsx_docs.md) | [View](webhooks-failed.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 234: packages/preview-server/scripts/utils/default-seed/marketing


**Folder Path:** `packages/preview-server/scripts/utils/default-seed/marketing`
**Generated:** 2025-11-15T20:38:37.833920Z

---

## Overview

This directory (`packages/preview-server/scripts/utils/default-seed/marketing`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains utility functions and helper modules.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/scripts/utils/default-seed/marketing



| File | Documentation | Keywords |
|------|---------------|----------|
| `changelog.tsx` | [View](changelog.tsx_docs.md) | [View](changelog.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 235: packages/preview-server/src


**Folder Path:** `packages/preview-server/src`
**Generated:** 2025-11-15T20:38:37.835324Z

---

## Overview

This directory (`packages/preview-server/src`) contains React components. 

## Structure

- **Subdirectories:** 7
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `actions/`
- `animated-icons-data/`
- `app/`
- `components/`
- `contexts/`
- `hooks/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src

---

# Chapter 236: packages/preview-server/src/actions


**Folder Path:** `packages/preview-server/src/actions`
**Generated:** 2025-11-15T20:38:37.836020Z

---

## Overview

This directory (`packages/preview-server/src/actions`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `email-validation/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/actions



| File | Documentation | Keywords |
|------|---------------|----------|
| `export-single-template.ts` | [View](export-single-template.ts_docs.md) | [View](export-single-template.ts_kw.md) |
| `get-email-path-from-slug.ts` | [View](get-email-path-from-slug.ts_docs.md) | [View](get-email-path-from-slug.ts_kw.md) |
| `get-emails-directory-metadata-action.ts` | [View](get-emails-directory-metadata-action.ts_docs.md) | [View](get-emails-directory-metadata-action.ts_kw.md) |
| `render-email-by-path.tsx` | [View](render-email-by-path.tsx_docs.md) | [View](render-email-by-path.tsx_kw.md) |
| `safe-action.ts` | [View](safe-action.ts_docs.md) | [View](safe-action.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 237: packages/preview-server/src/actions/email-validation


**Folder Path:** `packages/preview-server/src/actions/email-validation`
**Generated:** 2025-11-15T20:38:37.838741Z

---

## Overview

This directory (`packages/preview-server/src/actions/email-validation`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 8
- **Keyword Files:** 8

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/actions/email-validation



| File | Documentation | Keywords |
|------|---------------|----------|
| `caniemail-data.ts` | [View](caniemail-data.ts_docs.md) | [View](caniemail-data.ts_kw.md) |
| `check-compatibility.ts` | [View](check-compatibility.ts_docs.md) | [View](check-compatibility.ts_kw.md) |
| `check-images.spec.tsx` | [View](check-images.spec.tsx_docs.md) | [View](check-images.spec.tsx_kw.md) |
| `check-images.ts` | [View](check-images.ts_docs.md) | [View](check-images.ts_kw.md) |
| `check-links.spec.tsx` | [View](check-links.spec.tsx_docs.md) | [View](check-links.spec.tsx_kw.md) |
| `check-links.ts` | [View](check-links.ts_docs.md) | [View](check-links.ts_kw.md) |
| `get-code-location-from-ast-element.ts` | [View](get-code-location-from-ast-element.ts_docs.md) | [View](get-code-location-from-ast-element.ts_kw.md) |
| `quick-fetch.ts` | [View](quick-fetch.ts_docs.md) | [View](quick-fetch.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 238: packages/preview-server/src/actions/email-validation/__snapshots__


**Folder Path:** `packages/preview-server/src/actions/email-validation/__snapshots__`
**Generated:** 2025-11-15T20:38:37.846557Z

---

## Overview

This directory (`packages/preview-server/src/actions/email-validation/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/actions/email-validation/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `check-images.spec.tsx.snap` | [View](check-images.spec.tsx.snap_docs.md) | [View](check-images.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 239: packages/preview-server/src/animated-icons-data


**Folder Path:** `packages/preview-server/src/animated-icons-data`
**Generated:** 2025-11-15T20:38:37.847674Z

---

## Overview

This directory (`packages/preview-server/src/animated-icons-data`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/animated-icons-data



| File | Documentation | Keywords |
|------|---------------|----------|
| `help.json` | [View](help.json_docs.md) | [View](help.json_kw.md) |
| `link.json` | [View](link.json_docs.md) | [View](link.json_kw.md) |
| `load.json` | [View](load.json_docs.md) | [View](load.json_kw.md) |
| `mail.json` | [View](mail.json_docs.md) | [View](mail.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 240: packages/preview-server/src/app


**Folder Path:** `packages/preview-server/src/app`
**Generated:** 2025-11-15T20:38:37.849395Z

---

## Overview

This directory (`packages/preview-server/src/app`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 7
- **Keyword Files:** 5

### Subdirectories

- `fonts/`
- `preview/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/app



| File | Documentation | Keywords |
|------|---------------|----------|
| `env.ts` | [View](env.ts_docs.md) | [View](env.ts_kw.md) |
| `favicon.ico` | [View](favicon.ico_docs.md) | - |
| `fonts.ts` | [View](fonts.ts_docs.md) | [View](fonts.ts_kw.md) |
| `globals.css` | [View](globals.css_docs.md) | [View](globals.css_kw.md) |
| `layout.tsx` | [View](layout.tsx_docs.md) | [View](layout.tsx_kw.md) |
| `logo.png` | [View](logo.png_docs.md) | - |
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 241: packages/preview-server/src/app/fonts


**Folder Path:** `packages/preview-server/src/app/fonts`
**Generated:** 2025-11-15T20:38:37.851672Z

---

## Overview

This directory (`packages/preview-server/src/app/fonts`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `SFMono/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/app/fonts

---

# Chapter 242: packages/preview-server/src/app/fonts/SFMono


**Folder Path:** `packages/preview-server/src/app/fonts/SFMono`
**Generated:** 2025-11-15T20:38:37.852400Z

---

## Overview

This directory (`packages/preview-server/src/app/fonts/SFMono`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 12
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/app/fonts/SFMono



| File | Documentation | Keywords |
|------|---------------|----------|
| `SFMonoBold.otf` | [View](SFMonoBold.otf_docs.md) | - |
| `SFMonoBoldItalic.otf` | [View](SFMonoBoldItalic.otf_docs.md) | - |
| `SFMonoHeavy.otf` | [View](SFMonoHeavy.otf_docs.md) | - |
| `SFMonoHeavyItalic.otf` | [View](SFMonoHeavyItalic.otf_docs.md) | - |
| `SFMonoLight.otf` | [View](SFMonoLight.otf_docs.md) | - |
| `SFMonoLightItalic.otf` | [View](SFMonoLightItalic.otf_docs.md) | - |
| `SFMonoMedium.otf` | [View](SFMonoMedium.otf_docs.md) | - |
| `SFMonoMediumItalic.otf` | [View](SFMonoMediumItalic.otf_docs.md) | - |
| `SFMonoRegular.otf` | [View](SFMonoRegular.otf_docs.md) | - |
| `SFMonoRegularItalic.otf` | [View](SFMonoRegularItalic.otf_docs.md) | - |
| `SFMonoSemibold.otf` | [View](SFMonoSemibold.otf_docs.md) | - |
| `SFMonoSemiboldItalic.otf` | [View](SFMonoSemiboldItalic.otf_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 243: packages/preview-server/src/app/preview


**Folder Path:** `packages/preview-server/src/app/preview`
**Generated:** 2025-11-15T20:38:37.853103Z

---

## Overview

This directory (`packages/preview-server/src/app/preview`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `[...slug]/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/app/preview

---

# Chapter 244: packages/preview-server/src/app/preview/[...slug]


**Folder Path:** `packages/preview-server/src/app/preview/[...slug]`
**Generated:** 2025-11-15T20:38:37.853839Z

---

## Overview

This directory (`packages/preview-server/src/app/preview/[...slug]`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/app/preview/[...slug]



| File | Documentation | Keywords |
|------|---------------|----------|
| `email-frame.tsx` | [View](email-frame.tsx_docs.md) | [View](email-frame.tsx_kw.md) |
| `error-overlay.tsx` | [View](error-overlay.tsx_docs.md) | [View](error-overlay.tsx_kw.md) |
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |
| `preview.tsx` | [View](preview.tsx_docs.md) | [View](preview.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 245: packages/preview-server/src/components


**Folder Path:** `packages/preview-server/src/components`
**Generated:** 2025-11-15T20:38:37.857999Z

---

## Overview

This directory (`packages/preview-server/src/components`) contains 

## Structure

- **Subdirectories:** 4
- **Documentation Files:** 15
- **Keyword Files:** 15

### Subdirectories

- `icons/`
- `sidebar/`
- `toolbar/`
- `topbar/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/components



| File | Documentation | Keywords |
|------|---------------|----------|
| `button.tsx` | [View](button.tsx_docs.md) | [View](button.tsx_kw.md) |
| `code-container.tsx` | [View](code-container.tsx_docs.md) | [View](code-container.tsx_kw.md) |
| `code-snippet.tsx` | [View](code-snippet.tsx_docs.md) | [View](code-snippet.tsx_kw.md) |
| `code.tsx` | [View](code.tsx_docs.md) | [View](code.tsx_kw.md) |
| `heading.tsx` | [View](heading.tsx_docs.md) | [View](heading.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `logo.tsx` | [View](logo.tsx_docs.md) | [View](logo.tsx_kw.md) |
| `resizable-wrapper.tsx` | [View](resizable-wrapper.tsx_docs.md) | [View](resizable-wrapper.tsx_kw.md) |
| `send.tsx` | [View](send.tsx_docs.md) | [View](send.tsx_kw.md) |
| `shell.tsx` | [View](shell.tsx_docs.md) | [View](shell.tsx_kw.md) |
| `text.tsx` | [View](text.tsx_docs.md) | [View](text.tsx_kw.md) |
| `toolbar.tsx` | [View](toolbar.tsx_docs.md) | [View](toolbar.tsx_kw.md) |
| `tooltip-content.tsx` | [View](tooltip-content.tsx_docs.md) | [View](tooltip-content.tsx_kw.md) |
| `tooltip.tsx` | [View](tooltip.tsx_docs.md) | [View](tooltip.tsx_kw.md) |
| `topbar.tsx` | [View](topbar.tsx_docs.md) | [View](topbar.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 246: packages/preview-server/src/components/icons


**Folder Path:** `packages/preview-server/src/components/icons`
**Generated:** 2025-11-15T20:38:37.865267Z

---

## Overview

This directory (`packages/preview-server/src/components/icons`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 26
- **Keyword Files:** 26

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/components/icons



| File | Documentation | Keywords |
|------|---------------|----------|
| `icon-arrow-down.tsx` | [View](icon-arrow-down.tsx_docs.md) | [View](icon-arrow-down.tsx_kw.md) |
| `icon-base.tsx` | [View](icon-base.tsx_docs.md) | [View](icon-base.tsx_kw.md) |
| `icon-bug.tsx` | [View](icon-bug.tsx_docs.md) | [View](icon-bug.tsx_kw.md) |
| `icon-button.tsx` | [View](icon-button.tsx_docs.md) | [View](icon-button.tsx_kw.md) |
| `icon-check.tsx` | [View](icon-check.tsx_docs.md) | [View](icon-check.tsx_kw.md) |
| `icon-clipboard.tsx` | [View](icon-clipboard.tsx_docs.md) | [View](icon-clipboard.tsx_kw.md) |
| `icon-cloud-alert.tsx` | [View](icon-cloud-alert.tsx_docs.md) | [View](icon-cloud-alert.tsx_kw.md) |
| `icon-cloud-check.tsx` | [View](icon-cloud-check.tsx_docs.md) | [View](icon-cloud-check.tsx_kw.md) |
| `icon-download.tsx` | [View](icon-download.tsx_docs.md) | [View](icon-download.tsx_kw.md) |
| `icon-email.tsx` | [View](icon-email.tsx_docs.md) | [View](icon-email.tsx_kw.md) |
| `icon-file.tsx` | [View](icon-file.tsx_docs.md) | [View](icon-file.tsx_kw.md) |
| `icon-folder-open.tsx` | [View](icon-folder-open.tsx_docs.md) | [View](icon-folder-open.tsx_kw.md) |
| `icon-folder.tsx` | [View](icon-folder.tsx_docs.md) | [View](icon-folder.tsx_kw.md) |
| `icon-hide-sidebar.tsx` | [View](icon-hide-sidebar.tsx_docs.md) | [View](icon-hide-sidebar.tsx_kw.md) |
| `icon-image.tsx` | [View](icon-image.tsx_docs.md) | [View](icon-image.tsx_kw.md) |
| `icon-info.tsx` | [View](icon-info.tsx_docs.md) | [View](icon-info.tsx_kw.md) |
| `icon-link.tsx` | [View](icon-link.tsx_docs.md) | [View](icon-link.tsx_kw.md) |
| `icon-loader.tsx` | [View](icon-loader.tsx_docs.md) | [View](icon-loader.tsx_kw.md) |
| `icon-monitor.tsx` | [View](icon-monitor.tsx_docs.md) | [View](icon-monitor.tsx_kw.md) |
| `icon-moon.tsx` | [View](icon-moon.tsx_docs.md) | [View](icon-moon.tsx_kw.md) |
| `icon-phone.tsx` | [View](icon-phone.tsx_docs.md) | [View](icon-phone.tsx_kw.md) |
| `icon-reload.tsx` | [View](icon-reload.tsx_docs.md) | [View](icon-reload.tsx_kw.md) |
| `icon-source.tsx` | [View](icon-source.tsx_docs.md) | [View](icon-source.tsx_kw.md) |
| `icon-stamp.tsx` | [View](icon-stamp.tsx_docs.md) | [View](icon-stamp.tsx_kw.md) |
| `icon-sun.tsx` | [View](icon-sun.tsx_docs.md) | [View](icon-sun.tsx_kw.md) |
| `icon-warning.tsx` | [View](icon-warning.tsx_docs.md) | [View](icon-warning.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 247: packages/preview-server/src/components/sidebar


**Folder Path:** `packages/preview-server/src/components/sidebar`
**Generated:** 2025-11-15T20:38:37.872988Z

---

## Overview

This directory (`packages/preview-server/src/components/sidebar`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/components/sidebar



| File | Documentation | Keywords |
|------|---------------|----------|
| `file-tree-directory-children.tsx` | [View](file-tree-directory-children.tsx_docs.md) | [View](file-tree-directory-children.tsx_kw.md) |
| `file-tree-directory.tsx` | [View](file-tree-directory.tsx_docs.md) | [View](file-tree-directory.tsx_kw.md) |
| `file-tree.tsx` | [View](file-tree.tsx_docs.md) | [View](file-tree.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `sidebar.tsx` | [View](sidebar.tsx_docs.md) | [View](sidebar.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 248: packages/preview-server/src/components/toolbar


**Folder Path:** `packages/preview-server/src/components/toolbar`
**Generated:** 2025-11-15T20:38:37.875836Z

---

## Overview

This directory (`packages/preview-server/src/components/toolbar`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 10
- **Keyword Files:** 10

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/components/toolbar



| File | Documentation | Keywords |
|------|---------------|----------|
| `checking-results.tsx` | [View](checking-results.tsx_docs.md) | [View](checking-results.tsx_kw.md) |
| `code-preview-line-link.tsx` | [View](code-preview-line-link.tsx_docs.md) | [View](code-preview-line-link.tsx_kw.md) |
| `compatibility.tsx` | [View](compatibility.tsx_docs.md) | [View](compatibility.tsx_kw.md) |
| `linter.tsx` | [View](linter.tsx_docs.md) | [View](linter.tsx_kw.md) |
| `resend.tsx` | [View](resend.tsx_docs.md) | [View](resend.tsx_kw.md) |
| `results-table.tsx` | [View](results-table.tsx_docs.md) | [View](results-table.tsx_kw.md) |
| `results.tsx` | [View](results.tsx_docs.md) | [View](results.tsx_kw.md) |
| `spam-assassin.tsx` | [View](spam-assassin.tsx_docs.md) | [View](spam-assassin.tsx_kw.md) |
| `toolbar-button.tsx` | [View](toolbar-button.tsx_docs.md) | [View](toolbar-button.tsx_kw.md) |
| `use-cached-state.ts` | [View](use-cached-state.ts_docs.md) | [View](use-cached-state.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 249: packages/preview-server/src/components/topbar


**Folder Path:** `packages/preview-server/src/components/topbar`
**Generated:** 2025-11-15T20:38:37.881524Z

---

## Overview

This directory (`packages/preview-server/src/components/topbar`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/components/topbar



| File | Documentation | Keywords |
|------|---------------|----------|
| `active-view-toggle-group.tsx` | [View](active-view-toggle-group.tsx_docs.md) | [View](active-view-toggle-group.tsx_kw.md) |
| `emulated-dark-mode-toggle.tsx` | [View](emulated-dark-mode-toggle.tsx_docs.md) | [View](emulated-dark-mode-toggle.tsx_kw.md) |
| `view-size-controls.tsx` | [View](view-size-controls.tsx_docs.md) | [View](view-size-controls.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 250: packages/preview-server/src/contexts


**Folder Path:** `packages/preview-server/src/contexts`
**Generated:** 2025-11-15T20:38:37.884387Z

---

## Overview

This directory (`packages/preview-server/src/contexts`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/contexts



| File | Documentation | Keywords |
|------|---------------|----------|
| `emails.tsx` | [View](emails.tsx_docs.md) | [View](emails.tsx_kw.md) |
| `preview.tsx` | [View](preview.tsx_docs.md) | [View](preview.tsx_kw.md) |
| `toolbar.tsx` | [View](toolbar.tsx_docs.md) | [View](toolbar.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 251: packages/preview-server/src/hooks


**Folder Path:** `packages/preview-server/src/hooks`
**Generated:** 2025-11-15T20:38:37.886277Z

---

## Overview

This directory (`packages/preview-server/src/hooks`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/hooks



| File | Documentation | Keywords |
|------|---------------|----------|
| `use-clamped-state.ts` | [View](use-clamped-state.ts_docs.md) | [View](use-clamped-state.ts_kw.md) |
| `use-email-rendering-result.ts` | [View](use-email-rendering-result.ts_docs.md) | [View](use-email-rendering-result.ts_kw.md) |
| `use-fragment-identifier.ts` | [View](use-fragment-identifier.ts_docs.md) | [View](use-fragment-identifier.ts_kw.md) |
| `use-hot-reload.ts` | [View](use-hot-reload.ts_docs.md) | [View](use-hot-reload.ts_kw.md) |
| `use-rendering-metadata.ts` | [View](use-rendering-metadata.ts_docs.md) | [View](use-rendering-metadata.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 252: packages/preview-server/src/utils


**Folder Path:** `packages/preview-server/src/utils`
**Generated:** 2025-11-15T20:38:37.889074Z

---

## Overview

This directory (`packages/preview-server/src/utils`) contains test files. 

## Structure

- **Subdirectories:** 5
- **Documentation Files:** 27
- **Keyword Files:** 27

### Subdirectories

- `__snapshots__/`
- `caniemail/`
- `esbuild/`
- `testing/`
- `types/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `cn.ts` | [View](cn.ts_docs.md) | [View](cn.ts_kw.md) |
| `constants.ts` | [View](constants.ts_docs.md) | [View](constants.ts_kw.md) |
| `contains-email-template.spec.ts` | [View](contains-email-template.spec.ts_docs.md) | [View](contains-email-template.spec.ts_kw.md) |
| `contains-email-template.ts` | [View](contains-email-template.ts_docs.md) | [View](contains-email-template.ts_kw.md) |
| `convert-stack-with-sourcemap.ts` | [View](convert-stack-with-sourcemap.ts_docs.md) | [View](convert-stack-with-sourcemap.ts_kw.md) |
| `copy-text-to-clipboard.ts` | [View](copy-text-to-clipboard.ts_docs.md) | [View](copy-text-to-clipboard.ts_kw.md) |
| `create-jsx-runtime.ts` | [View](create-jsx-runtime.ts_docs.md) | [View](create-jsx-runtime.ts_kw.md) |
| `get-email-component.spec.ts` | [View](get-email-component.spec.ts_docs.md) | [View](get-email-component.spec.ts_kw.md) |
| `get-email-component.ts` | [View](get-email-component.ts_docs.md) | [View](get-email-component.ts_kw.md) |
| `get-emails-directory-metadata.spec.ts` | [View](get-emails-directory-metadata.spec.ts_docs.md) | [View](get-emails-directory-metadata.spec.ts_kw.md) |
| `get-emails-directory-metadata.ts` | [View](get-emails-directory-metadata.ts_docs.md) | [View](get-emails-directory-metadata.ts_kw.md) |
| `get-line-and-column-from-offset.spec.ts` | [View](get-line-and-column-from-offset.spec.ts_docs.md) | [View](get-line-and-column-from-offset.spec.ts_kw.md) |
| `get-line-and-column-from-offset.ts` | [View](get-line-and-column-from-offset.ts_docs.md) | [View](get-line-and-column-from-offset.ts_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `js-email-detection.spec.ts` | [View](js-email-detection.spec.ts_docs.md) | [View](js-email-detection.spec.ts_kw.md) |
| `language-map.ts` | [View](language-map.ts_docs.md) | [View](language-map.ts_kw.md) |
| `linting.ts` | [View](linting.ts_docs.md) | [View](linting.ts_kw.md) |
| `load-stream.ts` | [View](load-stream.ts_docs.md) | [View](load-stream.ts_kw.md) |
| `register-spinner-autostopping.ts` | [View](register-spinner-autostopping.ts_docs.md) | [View](register-spinner-autostopping.ts_kw.md) |
| `result.ts` | [View](result.ts_docs.md) | [View](result.ts_kw.md) |
| `run-bundled-code.ts` | [View](run-bundled-code.ts_docs.md) | [View](run-bundled-code.ts_kw.md) |
| `sanitize.ts` | [View](sanitize.ts_docs.md) | [View](sanitize.ts_kw.md) |
| `sleep.ts` | [View](sleep.ts_docs.md) | [View](sleep.ts_kw.md) |
| `snake-to-camel.ts` | [View](snake-to-camel.ts_docs.md) | [View](snake-to-camel.ts_kw.md) |
| `static-node-modules-for-vm.ts` | [View](static-node-modules-for-vm.ts_docs.md) | [View](static-node-modules-for-vm.ts_kw.md) |
| `style-text.ts` | [View](style-text.ts_docs.md) | [View](style-text.ts_kw.md) |
| `unreachable.ts` | [View](unreachable.ts_docs.md) | [View](unreachable.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 253: packages/preview-server/src/utils/__snapshots__


**Folder Path:** `packages/preview-server/src/utils/__snapshots__`
**Generated:** 2025-11-15T20:38:37.898685Z

---

## Overview

This directory (`packages/preview-server/src/utils/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-email-component.spec.ts.snap` | [View](get-email-component.spec.ts.snap_docs.md) | [View](get-email-component.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 254: packages/preview-server/src/utils/caniemail


**Folder Path:** `packages/preview-server/src/utils/caniemail`
**Generated:** 2025-11-15T20:38:37.900161Z

---

## Overview

This directory (`packages/preview-server/src/utils/caniemail`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 8
- **Keyword Files:** 8

### Subdirectories

- `ast/`
- `tailwind/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/caniemail



| File | Documentation | Keywords |
|------|---------------|----------|
| `all-css-properties.ts` | [View](all-css-properties.ts_docs.md) | [View](all-css-properties.ts_kw.md) |
| `get-compatibility-stats-for-entry.ts` | [View](get-compatibility-stats-for-entry.ts_docs.md) | [View](get-compatibility-stats-for-entry.ts_kw.md) |
| `get-css-functions.ts` | [View](get-css-functions.ts_docs.md) | [View](get-css-functions.ts_kw.md) |
| `get-css-property-names.ts` | [View](get-css-property-names.ts_docs.md) | [View](get-css-property-names.ts_kw.md) |
| `get-css-property-with-value.ts` | [View](get-css-property-with-value.ts_docs.md) | [View](get-css-property-with-value.ts_kw.md) |
| `get-css-unit.ts` | [View](get-css-unit.ts_docs.md) | [View](get-css-unit.ts_kw.md) |
| `get-element-attributes.ts` | [View](get-element-attributes.ts_docs.md) | [View](get-element-attributes.ts_kw.md) |
| `get-element-names.ts` | [View](get-element-names.ts_docs.md) | [View](get-element-names.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 255: packages/preview-server/src/utils/caniemail/ast


**Folder Path:** `packages/preview-server/src/utils/caniemail/ast`
**Generated:** 2025-11-15T20:38:37.903619Z

---

## Overview

This directory (`packages/preview-server/src/utils/caniemail/ast`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/caniemail/ast



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-object-variables.spec.ts` | [View](get-object-variables.spec.ts_docs.md) | [View](get-object-variables.spec.ts_kw.md) |
| `get-object-variables.ts` | [View](get-object-variables.ts_docs.md) | [View](get-object-variables.ts_kw.md) |
| `get-used-style-properties.spec.ts` | [View](get-used-style-properties.spec.ts_docs.md) | [View](get-used-style-properties.spec.ts_kw.md) |
| `get-used-style-properties.ts` | [View](get-used-style-properties.ts_docs.md) | [View](get-used-style-properties.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 256: packages/preview-server/src/utils/caniemail/ast/__snapshots__


**Folder Path:** `packages/preview-server/src/utils/caniemail/ast/__snapshots__`
**Generated:** 2025-11-15T20:38:37.905936Z

---

## Overview

This directory (`packages/preview-server/src/utils/caniemail/ast/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/caniemail/ast/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-object-variables.spec.ts.snap` | [View](get-object-variables.spec.ts.snap_docs.md) | [View](get-object-variables.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 257: packages/preview-server/src/utils/caniemail/tailwind


**Folder Path:** `packages/preview-server/src/utils/caniemail/tailwind`
**Generated:** 2025-11-15T20:38:37.907090Z

---

## Overview

This directory (`packages/preview-server/src/utils/caniemail/tailwind`) contains test files. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `tests/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/caniemail/tailwind



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-tailwind-config.spec.ts` | [View](get-tailwind-config.spec.ts_docs.md) | [View](get-tailwind-config.spec.ts_kw.md) |
| `get-tailwind-config.ts` | [View](get-tailwind-config.ts_docs.md) | [View](get-tailwind-config.ts_kw.md) |
| `get-tailwind-metadata.spec.ts` | [View](get-tailwind-metadata.spec.ts_docs.md) | [View](get-tailwind-metadata.spec.ts_kw.md) |
| `get-tailwind-metadata.ts` | [View](get-tailwind-metadata.ts_docs.md) | [View](get-tailwind-metadata.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 258: packages/preview-server/src/utils/caniemail/tailwind/tests


**Folder Path:** `packages/preview-server/src/utils/caniemail/tailwind/tests`
**Generated:** 2025-11-15T20:38:37.909586Z

---

## Overview

This directory (`packages/preview-server/src/utils/caniemail/tailwind/tests`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/caniemail/tailwind/tests



| File | Documentation | Keywords |
|------|---------------|----------|
| `dummy-email-template.tsx` | [View](dummy-email-template.tsx_docs.md) | [View](dummy-email-template.tsx_kw.md) |
| `tailwind.config.ts` | [View](tailwind.config.ts_docs.md) | [View](tailwind.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 259: packages/preview-server/src/utils/esbuild


**Folder Path:** `packages/preview-server/src/utils/esbuild`
**Generated:** 2025-11-15T20:38:37.910925Z

---

## Overview

This directory (`packages/preview-server/src/utils/esbuild`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/esbuild



| File | Documentation | Keywords |
|------|---------------|----------|
| `escape-string-for-regex.ts` | [View](escape-string-for-regex.ts_docs.md) | [View](escape-string-for-regex.ts_kw.md) |
| `renderring-utilities-exporter.ts` | [View](renderring-utilities-exporter.ts_docs.md) | [View](renderring-utilities-exporter.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 260: packages/preview-server/src/utils/testing


**Folder Path:** `packages/preview-server/src/utils/testing`
**Generated:** 2025-11-15T20:38:37.912617Z

---

## Overview

This directory (`packages/preview-server/src/utils/testing`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/testing



| File | Documentation | Keywords |
|------|---------------|----------|
| `js-email-export-default.js` | [View](js-email-export-default.js_docs.md) | [View](js-email-export-default.js_kw.md) |
| `js-email-test.js` | [View](js-email-test.js_docs.md) | [View](js-email-test.js_kw.md) |
| `mdx-email-test.js` | [View](mdx-email-test.js_docs.md) | [View](mdx-email-test.js_kw.md) |
| `request-response-email.tsx` | [View](request-response-email.tsx_docs.md) | [View](request-response-email.tsx_kw.md) |
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 261: packages/preview-server/src/utils/types


**Folder Path:** `packages/preview-server/src/utils/types`
**Generated:** 2025-11-15T20:38:37.915432Z

---

## Overview

This directory (`packages/preview-server/src/utils/types`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview-server/src/utils/types



| File | Documentation | Keywords |
|------|---------------|----------|
| `as.ts` | [View](as.ts_docs.md) | [View](as.ts_kw.md) |
| `email-template.ts` | [View](email-template.ts_docs.md) | [View](email-template.ts_kw.md) |
| `error-object.ts` | [View](error-object.ts_docs.md) | [View](error-object.ts_kw.md) |
| `hot-reload-change.ts` | [View](hot-reload-change.ts_docs.md) | [View](hot-reload-change.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 262: packages/preview/src


**Folder Path:** `packages/preview/src`
**Generated:** 2025-11-15T20:38:37.917239Z

---

## Overview

This directory (`packages/preview/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `preview.spec.tsx` | [View](preview.spec.tsx_docs.md) | [View](preview.spec.tsx_kw.md) |
| `preview.tsx` | [View](preview.tsx_docs.md) | [View](preview.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 263: packages/preview/src/__snapshots__


**Folder Path:** `packages/preview/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.919110Z

---

## Overview

This directory (`packages/preview/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/preview/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `preview.spec.tsx.snap` | [View](preview.spec.tsx.snap_docs.md) | [View](preview.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 264: packages/react-email


**Folder Path:** `packages/react-email`
**Generated:** 2025-11-15T20:38:37.920158Z

---

## Overview

This directory (`packages/react-email`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 9
- **Keyword Files:** 9

### Subdirectories

- `dev/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `.npmignore` | [View](.npmignore_docs.md) | [View](.npmignore_kw.md) |
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `tsdown.config.ts` | [View](tsdown.config.ts_docs.md) | [View](tsdown.config.ts_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 265: packages/react-email/dev


**Folder Path:** `packages/react-email/dev`
**Generated:** 2025-11-15T20:38:37.923942Z

---

## Overview

This directory (`packages/react-email/dev`) contains a Node.js package. 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/dev



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `index.js` | [View](index.js_docs.md) | [View](index.js_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 266: packages/react-email/src


**Folder Path:** `packages/react-email/src`
**Generated:** 2025-11-15T20:38:37.925549Z

---

## Overview

This directory (`packages/react-email/src`) contains 

## Structure

- **Subdirectories:** 4
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `actions/`
- `cli/`
- `commands/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 267: packages/react-email/src/actions


**Folder Path:** `packages/react-email/src/actions`
**Generated:** 2025-11-15T20:38:37.926866Z

---

## Overview

This directory (`packages/react-email/src/actions`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `email-validation/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/actions

---

# Chapter 268: packages/react-email/src/actions/email-validation


**Folder Path:** `packages/react-email/src/actions/email-validation`
**Generated:** 2025-11-15T20:38:37.927826Z

---

## Overview

This directory (`packages/react-email/src/actions/email-validation`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/actions/email-validation

---

# Chapter 269: packages/react-email/src/actions/email-validation/__snapshots__


**Folder Path:** `packages/react-email/src/actions/email-validation/__snapshots__`
**Generated:** 2025-11-15T20:38:37.928665Z

---

## Overview

This directory (`packages/react-email/src/actions/email-validation/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/actions/email-validation/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `check-images.spec.tsx.snap` | [View](check-images.spec.tsx.snap_docs.md) | [View](check-images.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 270: packages/react-email/src/cli


**Folder Path:** `packages/react-email/src/cli`
**Generated:** 2025-11-15T20:38:37.929842Z

---

## Overview

This directory (`packages/react-email/src/cli`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli

---

# Chapter 271: packages/react-email/src/cli/utils


**Folder Path:** `packages/react-email/src/cli/utils`
**Generated:** 2025-11-15T20:38:37.930706Z

---

## Overview

This directory (`packages/react-email/src/cli/utils`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `preview/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils

---

# Chapter 272: packages/react-email/src/cli/utils/preview


**Folder Path:** `packages/react-email/src/cli/utils/preview`
**Generated:** 2025-11-15T20:38:37.931622Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `hot-reloading/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview

---

# Chapter 273: packages/react-email/src/cli/utils/preview/hot-reloading


**Folder Path:** `packages/react-email/src/cli/utils/preview/hot-reloading`
**Generated:** 2025-11-15T20:38:37.932535Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview/hot-reloading`) contains test files. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `__snapshots__/`
- `test/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview/hot-reloading

---

# Chapter 274: packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__


**Folder Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__`
**Generated:** 2025-11-15T20:38:37.933679Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `create-dependency-graph.spec.ts.snap` | [View](create-dependency-graph.spec.ts.snap_docs.md) | [View](create-dependency-graph.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 275: packages/react-email/src/cli/utils/preview/hot-reloading/test


**Folder Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/test`
**Generated:** 2025-11-15T20:38:37.935310Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview/hot-reloading/test`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `dependency-graph/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview/hot-reloading/test

---

# Chapter 276: packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph


**Folder Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph`
**Generated:** 2025-11-15T20:38:37.936415Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `inner/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph



| File | Documentation | Keywords |
|------|---------------|----------|
| `outer.ts` | [View](outer.ts_docs.md) | [View](outer.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 277: packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner


**Folder Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner`
**Generated:** 2025-11-15T20:38:37.938107Z

---

## Overview

This directory (`packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner



| File | Documentation | Keywords |
|------|---------------|----------|
| `data-to-import.json` | [View](data-to-import.json_docs.md) | [View](data-to-import.json_kw.md) |
| `file-a.ts` | [View](file-a.ts_docs.md) | [View](file-a.ts_kw.md) |
| `file-b.ts` | [View](file-b.ts_docs.md) | [View](file-b.ts_kw.md) |
| `general-importing-file.ts` | [View](general-importing-file.ts_docs.md) | [View](general-importing-file.ts_kw.md) |
| `outer-dependency.ts` | [View](outer-dependency.ts_docs.md) | [View](outer-dependency.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 278: packages/react-email/src/commands


**Folder Path:** `packages/react-email/src/commands`
**Generated:** 2025-11-15T20:38:37.940391Z

---

## Overview

This directory (`packages/react-email/src/commands`) contains test files. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `resend/`
- `testing/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/commands



| File | Documentation | Keywords |
|------|---------------|----------|
| `.npmignore` | [View](.npmignore_docs.md) | [View](.npmignore_kw.md) |
| `build.ts` | [View](build.ts_docs.md) | [View](build.ts_kw.md) |
| `dev.ts` | [View](dev.ts_docs.md) | [View](dev.ts_kw.md) |
| `export.ts` | [View](export.ts_docs.md) | [View](export.ts_kw.md) |
| `start.ts` | [View](start.ts_docs.md) | [View](start.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 279: packages/react-email/src/commands/resend


**Folder Path:** `packages/react-email/src/commands/resend`
**Generated:** 2025-11-15T20:38:37.943387Z

---

## Overview

This directory (`packages/react-email/src/commands/resend`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/commands/resend



| File | Documentation | Keywords |
|------|---------------|----------|
| `reset.ts` | [View](reset.ts_docs.md) | [View](reset.ts_kw.md) |
| `setup.ts` | [View](setup.ts_docs.md) | [View](setup.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 280: packages/react-email/src/commands/testing


**Folder Path:** `packages/react-email/src/commands/testing`
**Generated:** 2025-11-15T20:38:37.944706Z

---

## Overview

This directory (`packages/react-email/src/commands/testing`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `__snapshots__/`
- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/commands/testing



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `export.spec.ts` | [View](export.spec.ts_docs.md) | [View](export.spec.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 281: packages/react-email/src/commands/testing/__snapshots__


**Folder Path:** `packages/react-email/src/commands/testing/__snapshots__`
**Generated:** 2025-11-15T20:38:37.946087Z

---

## Overview

This directory (`packages/react-email/src/commands/testing/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/commands/testing/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `export.spec.ts.snap` | [View](export.spec.ts.snap_docs.md) | [View](export.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 282: packages/react-email/src/commands/testing/emails


**Folder Path:** `packages/react-email/src/commands/testing/emails`
**Generated:** 2025-11-15T20:38:37.947517Z

---

## Overview

This directory (`packages/react-email/src/commands/testing/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/commands/testing/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 283: packages/react-email/src/utils


**Folder Path:** `packages/react-email/src/utils`
**Generated:** 2025-11-15T20:38:37.948902Z

---

## Overview

This directory (`packages/react-email/src/utils`) contains 

## Structure

- **Subdirectories:** 4
- **Documentation Files:** 10
- **Keyword Files:** 10

### Subdirectories

- `__snapshots__/`
- `esbuild/`
- `preview/`
- `types/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `conf.ts` | [View](conf.ts_docs.md) | [View](conf.ts_kw.md) |
| `get-emails-directory-metadata.spec.ts` | [View](get-emails-directory-metadata.spec.ts_docs.md) | [View](get-emails-directory-metadata.spec.ts_kw.md) |
| `get-emails-directory-metadata.ts` | [View](get-emails-directory-metadata.ts_docs.md) | [View](get-emails-directory-metadata.ts_kw.md) |
| `get-preview-server-location.ts` | [View](get-preview-server-location.ts_docs.md) | [View](get-preview-server-location.ts_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `packageJson.ts` | [View](packageJson.ts_docs.md) | [View](packageJson.ts_kw.md) |
| `register-spinner-autostopping.ts` | [View](register-spinner-autostopping.ts_docs.md) | [View](register-spinner-autostopping.ts_kw.md) |
| `style-text.ts` | [View](style-text.ts_docs.md) | [View](style-text.ts_kw.md) |
| `tree.spec.ts` | [View](tree.spec.ts_docs.md) | [View](tree.spec.ts_kw.md) |
| `tree.ts` | [View](tree.ts_docs.md) | [View](tree.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 284: packages/react-email/src/utils/__snapshots__


**Folder Path:** `packages/react-email/src/utils/__snapshots__`
**Generated:** 2025-11-15T20:38:37.953013Z

---

## Overview

This directory (`packages/react-email/src/utils/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `tree.spec.ts.snap` | [View](tree.spec.ts.snap_docs.md) | [View](tree.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 285: packages/react-email/src/utils/esbuild


**Folder Path:** `packages/react-email/src/utils/esbuild`
**Generated:** 2025-11-15T20:38:37.954126Z

---

## Overview

This directory (`packages/react-email/src/utils/esbuild`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/esbuild



| File | Documentation | Keywords |
|------|---------------|----------|
| `escape-string-for-regex.ts` | [View](escape-string-for-regex.ts_docs.md) | [View](escape-string-for-regex.ts_kw.md) |
| `renderring-utilities-exporter.ts` | [View](renderring-utilities-exporter.ts_docs.md) | [View](renderring-utilities-exporter.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 286: packages/react-email/src/utils/preview


**Folder Path:** `packages/react-email/src/utils/preview`
**Generated:** 2025-11-15T20:38:37.955674Z

---

## Overview

This directory (`packages/react-email/src/utils/preview`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `hot-reloading/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview



| File | Documentation | Keywords |
|------|---------------|----------|
| `get-env-variables-for-preview-app.ts` | [View](get-env-variables-for-preview-app.ts_docs.md) | [View](get-env-variables-for-preview-app.ts_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `serve-static-file.ts` | [View](serve-static-file.ts_docs.md) | [View](serve-static-file.ts_kw.md) |
| `start-dev-server.ts` | [View](start-dev-server.ts_docs.md) | [View](start-dev-server.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 287: packages/react-email/src/utils/preview/hot-reloading


**Folder Path:** `packages/react-email/src/utils/preview/hot-reloading`
**Generated:** 2025-11-15T20:38:37.958271Z

---

## Overview

This directory (`packages/react-email/src/utils/preview/hot-reloading`) contains test files. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 7
- **Keyword Files:** 7

### Subdirectories

- `__snapshots__/`
- `test/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview/hot-reloading



| File | Documentation | Keywords |
|------|---------------|----------|
| `create-dependency-graph.spec.ts` | [View](create-dependency-graph.spec.ts_docs.md) | [View](create-dependency-graph.spec.ts_kw.md) |
| `create-dependency-graph.ts` | [View](create-dependency-graph.ts_docs.md) | [View](create-dependency-graph.ts_kw.md) |
| `get-imported-modules.spec.ts` | [View](get-imported-modules.spec.ts_docs.md) | [View](get-imported-modules.spec.ts_kw.md) |
| `get-imported-modules.ts` | [View](get-imported-modules.ts_docs.md) | [View](get-imported-modules.ts_kw.md) |
| `resolve-path-aliases.spec.ts` | [View](resolve-path-aliases.spec.ts_docs.md) | [View](resolve-path-aliases.spec.ts_kw.md) |
| `resolve-path-aliases.ts` | [View](resolve-path-aliases.ts_docs.md) | [View](resolve-path-aliases.ts_kw.md) |
| `setup-hot-reloading.ts` | [View](setup-hot-reloading.ts_docs.md) | [View](setup-hot-reloading.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 288: packages/react-email/src/utils/preview/hot-reloading/__snapshots__


**Folder Path:** `packages/react-email/src/utils/preview/hot-reloading/__snapshots__`
**Generated:** 2025-11-15T20:38:37.962138Z

---

## Overview

This directory (`packages/react-email/src/utils/preview/hot-reloading/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview/hot-reloading/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `create-dependency-graph.spec.ts.snap` | [View](create-dependency-graph.spec.ts.snap_docs.md) | [View](create-dependency-graph.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 289: packages/react-email/src/utils/preview/hot-reloading/test


**Folder Path:** `packages/react-email/src/utils/preview/hot-reloading/test`
**Generated:** 2025-11-15T20:38:37.963306Z

---

## Overview

This directory (`packages/react-email/src/utils/preview/hot-reloading/test`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `dependency-graph/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview/hot-reloading/test



| File | Documentation | Keywords |
|------|---------------|----------|
| `some-file.ts` | [View](some-file.ts_docs.md) | [View](some-file.ts_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 290: packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph


**Folder Path:** `packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph`
**Generated:** 2025-11-15T20:38:37.964536Z

---

## Overview

This directory (`packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `inner/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph



| File | Documentation | Keywords |
|------|---------------|----------|
| `outer.ts` | [View](outer.ts_docs.md) | [View](outer.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 291: packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph/inner


**Folder Path:** `packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph/inner`
**Generated:** 2025-11-15T20:38:37.965757Z

---

## Overview

This directory (`packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph/inner`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 5
- **Keyword Files:** 5

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/preview/hot-reloading/test/dependency-graph/inner



| File | Documentation | Keywords |
|------|---------------|----------|
| `data-to-import.json` | [View](data-to-import.json_docs.md) | [View](data-to-import.json_kw.md) |
| `file-a.ts` | [View](file-a.ts_docs.md) | [View](file-a.ts_kw.md) |
| `file-b.ts` | [View](file-b.ts_docs.md) | [View](file-b.ts_kw.md) |
| `general-importing-file.ts` | [View](general-importing-file.ts_docs.md) | [View](general-importing-file.ts_kw.md) |
| `outer-dependency.ts` | [View](outer-dependency.ts_docs.md) | [View](outer-dependency.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 292: packages/react-email/src/utils/types


**Folder Path:** `packages/react-email/src/utils/types`
**Generated:** 2025-11-15T20:38:37.967991Z

---

## Overview

This directory (`packages/react-email/src/utils/types`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/react-email/src/utils/types



| File | Documentation | Keywords |
|------|---------------|----------|
| `hot-reload-change.ts` | [View](hot-reload-change.ts_docs.md) | [View](hot-reload-change.ts_kw.md) |
| `hot-reload-event.ts` | [View](hot-reload-event.ts_docs.md) | [View](hot-reload-event.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 293: packages/render


**Folder Path:** `packages/render`
**Generated:** 2025-11-15T20:38:37.969121Z

---

## Overview

This directory (`packages/render`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 6
- **Keyword Files:** 6

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `tsdown.config.ts` | [View](tsdown.config.ts_docs.md) | [View](tsdown.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 294: packages/render/src


**Folder Path:** `packages/render/src`
**Generated:** 2025-11-15T20:38:37.971757Z

---

## Overview

This directory (`packages/render/src`) contains 

## Structure

- **Subdirectories:** 4
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `browser/`
- `edge/`
- `node/`
- `shared/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `react-internals.d.ts` | [View](react-internals.d.ts_docs.md) | [View](react-internals.d.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 295: packages/render/src/browser


**Folder Path:** `packages/render/src/browser`
**Generated:** 2025-11-15T20:38:37.972714Z

---

## Overview

This directory (`packages/render/src/browser`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/browser



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `render-web.spec.tsx` | [View](render-web.spec.tsx_docs.md) | [View](render-web.spec.tsx_kw.md) |
| `render.tsx` | [View](render.tsx_docs.md) | [View](render.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 296: packages/render/src/browser/__snapshots__


**Folder Path:** `packages/render/src/browser/__snapshots__`
**Generated:** 2025-11-15T20:38:37.974694Z

---

## Overview

This directory (`packages/render/src/browser/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/browser/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `render-web.spec.tsx.snap` | [View](render-web.spec.tsx.snap_docs.md) | [View](render-web.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 297: packages/render/src/edge


**Folder Path:** `packages/render/src/edge`
**Generated:** 2025-11-15T20:38:37.975988Z

---

## Overview

This directory (`packages/render/src/edge`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 4
- **Keyword Files:** 4

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/edge



| File | Documentation | Keywords |
|------|---------------|----------|
| `import-react-dom.tsx` | [View](import-react-dom.tsx_docs.md) | [View](import-react-dom.tsx_kw.md) |
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `render.spec.tsx` | [View](render.spec.tsx_docs.md) | [View](render.spec.tsx_kw.md) |
| `render.tsx` | [View](render.tsx_docs.md) | [View](render.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 298: packages/render/src/edge/__snapshots__


**Folder Path:** `packages/render/src/edge/__snapshots__`
**Generated:** 2025-11-15T20:38:37.978081Z

---

## Overview

This directory (`packages/render/src/edge/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/edge/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `render.spec.tsx.snap` | [View](render.spec.tsx.snap_docs.md) | [View](render.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 299: packages/render/src/node


**Folder Path:** `packages/render/src/node`
**Generated:** 2025-11-15T20:38:37.979157Z

---

## Overview

This directory (`packages/render/src/node`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 6
- **Keyword Files:** 6

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/node



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `read-stream.spec.ts` | [View](read-stream.spec.ts_docs.md) | [View](read-stream.spec.ts_kw.md) |
| `read-stream.ts` | [View](read-stream.ts_docs.md) | [View](read-stream.ts_kw.md) |
| `render-edge.spec.tsx` | [View](render-edge.spec.tsx_docs.md) | [View](render-edge.spec.tsx_kw.md) |
| `render-node.spec.tsx` | [View](render-node.spec.tsx_docs.md) | [View](render-node.spec.tsx_kw.md) |
| `render.tsx` | [View](render.tsx_docs.md) | [View](render.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 300: packages/render/src/node/__snapshots__


**Folder Path:** `packages/render/src/node/__snapshots__`
**Generated:** 2025-11-15T20:38:37.982866Z

---

## Overview

This directory (`packages/render/src/node/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/node/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `render-async-edge.spec.tsx.snap` | [View](render-async-edge.spec.tsx.snap_docs.md) | [View](render-async-edge.spec.tsx.snap_kw.md) |
| `render-async-node.spec.tsx.snap` | [View](render-async-node.spec.tsx.snap_docs.md) | [View](render-async-node.spec.tsx.snap_kw.md) |
| `render-edge.spec.tsx.snap` | [View](render-edge.spec.tsx.snap_docs.md) | [View](render-edge.spec.tsx.snap_kw.md) |
| `render-node.spec.tsx.snap` | [View](render-node.spec.tsx.snap_docs.md) | [View](render-node.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 301: packages/render/src/shared


**Folder Path:** `packages/render/src/shared`
**Generated:** 2025-11-15T20:38:37.985226Z

---

## Overview

This directory (`packages/render/src/shared`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 2
- **Keyword Files:** 2

### Subdirectories

- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/shared



| File | Documentation | Keywords |
|------|---------------|----------|
| `options.ts` | [View](options.ts_docs.md) | [View](options.ts_kw.md) |
| `read-stream.browser.ts` | [View](read-stream.browser.ts_docs.md) | [View](read-stream.browser.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 302: packages/render/src/shared/utils


**Folder Path:** `packages/render/src/shared/utils`
**Generated:** 2025-11-15T20:38:37.986504Z

---

## Overview

This directory (`packages/render/src/shared/utils`) contains test files. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `testing/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/shared/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `pretty.spec.ts` | [View](pretty.spec.ts_docs.md) | [View](pretty.spec.ts_kw.md) |
| `pretty.ts` | [View](pretty.ts_docs.md) | [View](pretty.ts_kw.md) |
| `to-plain-text.ts` | [View](to-plain-text.ts_docs.md) | [View](to-plain-text.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 303: packages/render/src/shared/utils/__snapshots__


**Folder Path:** `packages/render/src/shared/utils/__snapshots__`
**Generated:** 2025-11-15T20:38:37.988157Z

---

## Overview

This directory (`packages/render/src/shared/utils/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/shared/utils/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `pretty.spec.ts.snap` | [View](pretty.spec.ts.snap_docs.md) | [View](pretty.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 304: packages/render/src/shared/utils/testing


**Folder Path:** `packages/render/src/shared/utils/testing`
**Generated:** 2025-11-15T20:38:37.989506Z

---

## Overview

This directory (`packages/render/src/shared/utils/testing`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/render/src/shared/utils/testing



| File | Documentation | Keywords |
|------|---------------|----------|
| `preview.tsx` | [View](preview.tsx_docs.md) | [View](preview.tsx_kw.md) |
| `stripe-email.html` | [View](stripe-email.html_docs.md) | [View](stripe-email.html_kw.md) |
| `template.tsx` | [View](template.tsx_docs.md) | [View](template.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 305: packages/row


**Folder Path:** `packages/row`
**Generated:** 2025-11-15T20:38:37.991426Z

---

## Overview

This directory (`packages/row`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/row



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 306: packages/row/src


**Folder Path:** `packages/row/src`
**Generated:** 2025-11-15T20:38:37.993456Z

---

## Overview

This directory (`packages/row/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/row/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `row.spec.tsx` | [View](row.spec.tsx_docs.md) | [View](row.spec.tsx_kw.md) |
| `row.tsx` | [View](row.tsx_docs.md) | [View](row.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 307: packages/row/src/__snapshots__


**Folder Path:** `packages/row/src/__snapshots__`
**Generated:** 2025-11-15T20:38:37.994803Z

---

## Overview

This directory (`packages/row/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/row/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `row.spec.tsx.snap` | [View](row.spec.tsx.snap_docs.md) | [View](row.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 308: packages/section


**Folder Path:** `packages/section`
**Generated:** 2025-11-15T20:38:37.995769Z

---

## Overview

This directory (`packages/section`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/section



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 309: packages/section/src


**Folder Path:** `packages/section/src`
**Generated:** 2025-11-15T20:38:37.998560Z

---

## Overview

This directory (`packages/section/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/section/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `section.spec.tsx` | [View](section.spec.tsx_docs.md) | [View](section.spec.tsx_kw.md) |
| `section.tsx` | [View](section.tsx_docs.md) | [View](section.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 310: packages/section/src/__snapshots__


**Folder Path:** `packages/section/src/__snapshots__`
**Generated:** 2025-11-15T20:38:38.000194Z

---

## Overview

This directory (`packages/section/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/section/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `section.spec.tsx.snap` | [View](section.spec.tsx.snap_docs.md) | [View](section.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 311: packages/tailwind


**Folder Path:** `packages/tailwind`
**Generated:** 2025-11-15T20:38:38.001275Z

---

## Overview

This directory (`packages/tailwind`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 7
- **Keyword Files:** 7

### Subdirectories

- `integrations/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `tsdown.config.ts` | [View](tsdown.config.ts_docs.md) | [View](tsdown.config.ts_kw.md) |
| `vitest.config.ts` | [View](vitest.config.ts_docs.md) | [View](vitest.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 312: packages/tailwind/integrations


**Folder Path:** `packages/tailwind/integrations`
**Generated:** 2025-11-15T20:38:38.005568Z

---

## Overview

This directory (`packages/tailwind/integrations`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 1
- **Keyword Files:** 1

### Subdirectories

- `nextjs/`
- `vite/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations



| File | Documentation | Keywords |
|------|---------------|----------|
| `integrations.spec.ts` | [View](integrations.spec.ts_docs.md) | [View](integrations.spec.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 313: packages/tailwind/integrations/nextjs


**Folder Path:** `packages/tailwind/integrations/nextjs`
**Generated:** 2025-11-15T20:38:38.006580Z

---

## Overview

This directory (`packages/tailwind/integrations/nextjs`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 6
- **Keyword Files:** 6

### Subdirectories

- `emails/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/nextjs



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `next-env.d.ts` | [View](next-env.d.ts_docs.md) | [View](next-env.d.ts_kw.md) |
| `next.config.mjs` | [View](next.config.mjs_docs.md) | [View](next.config.mjs_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 314: packages/tailwind/integrations/nextjs/emails


**Folder Path:** `packages/tailwind/integrations/nextjs/emails`
**Generated:** 2025-11-15T20:38:38.009042Z

---

## Overview

This directory (`packages/tailwind/integrations/nextjs/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/nextjs/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 315: packages/tailwind/integrations/nextjs/src


**Folder Path:** `packages/tailwind/integrations/nextjs/src`
**Generated:** 2025-11-15T20:38:38.010209Z

---

## Overview

This directory (`packages/tailwind/integrations/nextjs/src`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `app/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/nextjs/src

---

# Chapter 316: packages/tailwind/integrations/nextjs/src/app


**Folder Path:** `packages/tailwind/integrations/nextjs/src/app`
**Generated:** 2025-11-15T20:38:38.010943Z

---

## Overview

This directory (`packages/tailwind/integrations/nextjs/src/app`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/nextjs/src/app



| File | Documentation | Keywords |
|------|---------------|----------|
| `favicon.ico` | [View](favicon.ico_docs.md) | - |
| `layout.tsx` | [View](layout.tsx_docs.md) | [View](layout.tsx_kw.md) |
| `page.tsx` | [View](page.tsx_docs.md) | [View](page.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 317: packages/tailwind/integrations/vite


**Folder Path:** `packages/tailwind/integrations/vite`
**Generated:** 2025-11-15T20:38:38.012329Z

---

## Overview

This directory (`packages/tailwind/integrations/vite`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 7
- **Keyword Files:** 7

### Subdirectories

- `emails/`
- `public/`
- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/vite



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `index.html` | [View](index.html_docs.md) | [View](index.html_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |
| `tsconfig.node.json` | [View](tsconfig.node.json_docs.md) | [View](tsconfig.node.json_kw.md) |
| `vite.config.ts` | [View](vite.config.ts_docs.md) | [View](vite.config.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 318: packages/tailwind/integrations/vite/emails


**Folder Path:** `packages/tailwind/integrations/vite/emails`
**Generated:** 2025-11-15T20:38:38.014823Z

---

## Overview

This directory (`packages/tailwind/integrations/vite/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/vite/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `vercel-invite-user.tsx` | [View](vercel-invite-user.tsx_docs.md) | [View](vercel-invite-user.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 319: packages/tailwind/integrations/vite/public


**Folder Path:** `packages/tailwind/integrations/vite/public`
**Generated:** 2025-11-15T20:38:38.015987Z

---

## Overview

This directory (`packages/tailwind/integrations/vite/public`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 0

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/vite/public



| File | Documentation | Keywords |
|------|---------------|----------|
| `vite.svg` | [View](vite.svg_docs.md) | - |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 320: packages/tailwind/integrations/vite/src


**Folder Path:** `packages/tailwind/integrations/vite/src`
**Generated:** 2025-11-15T20:38:38.016659Z

---

## Overview

This directory (`packages/tailwind/integrations/vite/src`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/integrations/vite/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `App.tsx` | [View](App.tsx_docs.md) | [View](App.tsx_kw.md) |
| `main.tsx` | [View](main.tsx_docs.md) | [View](main.tsx_kw.md) |
| `vite-env.d.ts` | [View](vite-env.d.ts_docs.md) | [View](vite-env.d.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 321: packages/tailwind/src


**Folder Path:** `packages/tailwind/src`
**Generated:** 2025-11-15T20:38:38.018218Z

---

## Overview

This directory (`packages/tailwind/src`) contains 

## Structure

- **Subdirectories:** 3
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `__snapshots__/`
- `hooks/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `inline-styles.ts` | [View](inline-styles.ts_docs.md) | [View](inline-styles.ts_kw.md) |
| `sanitize-stylesheet.ts` | [View](sanitize-stylesheet.ts_docs.md) | [View](sanitize-stylesheet.ts_kw.md) |
| `tailwind.spec.tsx` | [View](tailwind.spec.tsx_docs.md) | [View](tailwind.spec.tsx_kw.md) |
| `tailwind.tsx` | [View](tailwind.tsx_docs.md) | [View](tailwind.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 322: packages/tailwind/src/__snapshots__


**Folder Path:** `packages/tailwind/src/__snapshots__`
**Generated:** 2025-11-15T20:38:38.021048Z

---

## Overview

This directory (`packages/tailwind/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `tailwind.spec.tsx.snap` | [View](tailwind.spec.tsx.snap_docs.md) | [View](tailwind.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 323: packages/tailwind/src/hooks


**Folder Path:** `packages/tailwind/src/hooks`
**Generated:** 2025-11-15T20:38:38.022609Z

---

## Overview

This directory (`packages/tailwind/src/hooks`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/hooks



| File | Documentation | Keywords |
|------|---------------|----------|
| `use-suspended-promise.ts` | [View](use-suspended-promise.ts_docs.md) | [View](use-suspended-promise.ts_kw.md) |
| `use-suspensed-promise.spec.ts` | [View](use-suspensed-promise.spec.ts_docs.md) | [View](use-suspensed-promise.spec.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 324: packages/tailwind/src/utils


**Folder Path:** `packages/tailwind/src/utils`
**Generated:** 2025-11-15T20:38:38.024276Z

---

## Overview

This directory (`packages/tailwind/src/utils`) contains 

## Structure

- **Subdirectories:** 6
- **Documentation Files:** 0
- **Keyword Files:** 0

### Subdirectories

- `__snapshots__/`
- `compatibility/`
- `css/`
- `react/`
- `tailwindcss/`
- `text/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils

---

# Chapter 325: packages/tailwind/src/utils/__snapshots__


**Folder Path:** `packages/tailwind/src/utils/__snapshots__`
**Generated:** 2025-11-15T20:38:38.024989Z

---

## Overview

This directory (`packages/tailwind/src/utils/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `quick-safe-render-to-string.spec.tsx.snap` | [View](quick-safe-render-to-string.spec.tsx.snap_docs.md) | [View](quick-safe-render-to-string.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 326: packages/tailwind/src/utils/compatibility


**Folder Path:** `packages/tailwind/src/utils/compatibility`
**Generated:** 2025-11-15T20:38:38.026004Z

---

## Overview

This directory (`packages/tailwind/src/utils/compatibility`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 6
- **Keyword Files:** 6

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/compatibility



| File | Documentation | Keywords |
|------|---------------|----------|
| `escape-class-name.spec.ts` | [View](escape-class-name.spec.ts_docs.md) | [View](escape-class-name.spec.ts_kw.md) |
| `escape-class-name.ts` | [View](escape-class-name.ts_docs.md) | [View](escape-class-name.ts_kw.md) |
| `get-react-property.ts` | [View](get-react-property.ts_docs.md) | [View](get-react-property.ts_kw.md) |
| `sanitize-class-name.spec.ts` | [View](sanitize-class-name.spec.ts_docs.md) | [View](sanitize-class-name.spec.ts_kw.md) |
| `sanitize-class-name.ts` | [View](sanitize-class-name.ts_docs.md) | [View](sanitize-class-name.ts_kw.md) |
| `unescape-class.ts` | [View](unescape-class.ts_docs.md) | [View](unescape-class.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 327: packages/tailwind/src/utils/css


**Folder Path:** `packages/tailwind/src/utils/css`
**Generated:** 2025-11-15T20:38:38.028300Z

---

## Overview

This directory (`packages/tailwind/src/utils/css`) contains 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 15
- **Keyword Files:** 15

### Subdirectories

- `__snapshots__/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/css



| File | Documentation | Keywords |
|------|---------------|----------|
| `extract-rules-per-class.spec.ts` | [View](extract-rules-per-class.spec.ts_docs.md) | [View](extract-rules-per-class.spec.ts_kw.md) |
| `extract-rules-per-class.ts` | [View](extract-rules-per-class.ts_docs.md) | [View](extract-rules-per-class.ts_kw.md) |
| `get-custom-properties.ts` | [View](get-custom-properties.ts_docs.md) | [View](get-custom-properties.ts_kw.md) |
| `is-rule-inlinable.ts` | [View](is-rule-inlinable.ts_docs.md) | [View](is-rule-inlinable.ts_kw.md) |
| `make-inline-styles-for.spec.ts` | [View](make-inline-styles-for.spec.ts_docs.md) | [View](make-inline-styles-for.spec.ts_kw.md) |
| `make-inline-styles-for.ts` | [View](make-inline-styles-for.ts_docs.md) | [View](make-inline-styles-for.ts_kw.md) |
| `resolve-all-css-variables.spec.ts` | [View](resolve-all-css-variables.spec.ts_docs.md) | [View](resolve-all-css-variables.spec.ts_kw.md) |
| `resolve-all-css-variables.ts` | [View](resolve-all-css-variables.ts_docs.md) | [View](resolve-all-css-variables.ts_kw.md) |
| `resolve-calc-expressions.spec.ts` | [View](resolve-calc-expressions.spec.ts_docs.md) | [View](resolve-calc-expressions.spec.ts_kw.md) |
| `resolve-calc-expressions.ts` | [View](resolve-calc-expressions.ts_docs.md) | [View](resolve-calc-expressions.ts_kw.md) |
| `sanitize-declarations.spec.ts` | [View](sanitize-declarations.spec.ts_docs.md) | [View](sanitize-declarations.spec.ts_kw.md) |
| `sanitize-declarations.ts` | [View](sanitize-declarations.ts_docs.md) | [View](sanitize-declarations.ts_kw.md) |
| `sanitize-non-inlinable-rules.spec.ts` | [View](sanitize-non-inlinable-rules.spec.ts_docs.md) | [View](sanitize-non-inlinable-rules.spec.ts_kw.md) |
| `sanitize-non-inlinable-rules.ts` | [View](sanitize-non-inlinable-rules.ts_docs.md) | [View](sanitize-non-inlinable-rules.ts_kw.md) |
| `unwrap-value.ts` | [View](unwrap-value.ts_docs.md) | [View](unwrap-value.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 328: packages/tailwind/src/utils/css/__snapshots__


**Folder Path:** `packages/tailwind/src/utils/css/__snapshots__`
**Generated:** 2025-11-15T20:38:38.034539Z

---

## Overview

This directory (`packages/tailwind/src/utils/css/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 9
- **Keyword Files:** 9

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/css/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `extract-rules-matching-classes.spec.ts.snap` | [View](extract-rules-matching-classes.spec.ts.snap_docs.md) | [View](extract-rules-matching-classes.spec.ts.snap_kw.md) |
| `extract-rules-per-class.spec.ts.snap` | [View](extract-rules-per-class.spec.ts.snap_docs.md) | [View](extract-rules-per-class.spec.ts.snap_kw.md) |
| `make-inline-styles-for.spec.ts.snap` | [View](make-inline-styles-for.spec.ts.snap_docs.md) | [View](make-inline-styles-for.spec.ts.snap_kw.md) |
| `remove-rule-duplicates-from-root.spec.ts.snap` | [View](remove-rule-duplicates-from-root.spec.ts.snap_docs.md) | [View](remove-rule-duplicates-from-root.spec.ts.snap_kw.md) |
| `resolve-all-css-variables.spec.ts.snap` | [View](resolve-all-css-variables.spec.ts.snap_docs.md) | [View](resolve-all-css-variables.spec.ts.snap_kw.md) |
| `resolve-calc-expressions.spec.ts.snap` | [View](resolve-calc-expressions.spec.ts.snap_docs.md) | [View](resolve-calc-expressions.spec.ts.snap_kw.md) |
| `sanitize-declarations.spec.ts.snap` | [View](sanitize-declarations.spec.ts.snap_docs.md) | [View](sanitize-declarations.spec.ts.snap_kw.md) |
| `sanitize-non-inlinable-classes.spec.ts.snap` | [View](sanitize-non-inlinable-classes.spec.ts.snap_docs.md) | [View](sanitize-non-inlinable-classes.spec.ts.snap_kw.md) |
| `sanitize-non-inlinable-rules.spec.ts.snap` | [View](sanitize-non-inlinable-rules.spec.ts.snap_docs.md) | [View](sanitize-non-inlinable-rules.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 329: packages/tailwind/src/utils/react


**Folder Path:** `packages/tailwind/src/utils/react`
**Generated:** 2025-11-15T20:38:38.038489Z

---

## Overview

This directory (`packages/tailwind/src/utils/react`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 3
- **Keyword Files:** 3

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/react



| File | Documentation | Keywords |
|------|---------------|----------|
| `is-component.ts` | [View](is-component.ts_docs.md) | [View](is-component.ts_kw.md) |
| `map-react-tree.spec.tsx` | [View](map-react-tree.spec.tsx_docs.md) | [View](map-react-tree.spec.tsx_kw.md) |
| `map-react-tree.ts` | [View](map-react-tree.ts_docs.md) | [View](map-react-tree.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 330: packages/tailwind/src/utils/tailwindcss


**Folder Path:** `packages/tailwind/src/utils/tailwindcss`
**Generated:** 2025-11-15T20:38:38.040404Z

---

## Overview

This directory (`packages/tailwind/src/utils/tailwindcss`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `tailwind-stylesheets/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/tailwindcss



| File | Documentation | Keywords |
|------|---------------|----------|
| `clone-element-with-inlined-styles.ts` | [View](clone-element-with-inlined-styles.ts_docs.md) | [View](clone-element-with-inlined-styles.ts_kw.md) |
| `setup-tailwind.spec.ts` | [View](setup-tailwind.spec.ts_docs.md) | [View](setup-tailwind.spec.ts_kw.md) |
| `setup-tailwind.ts` | [View](setup-tailwind.ts_docs.md) | [View](setup-tailwind.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 331: packages/tailwind/src/utils/tailwindcss/__snapshots__


**Folder Path:** `packages/tailwind/src/utils/tailwindcss/__snapshots__`
**Generated:** 2025-11-15T20:38:38.042158Z

---

## Overview

This directory (`packages/tailwind/src/utils/tailwindcss/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/tailwindcss/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `setup-tailwind.spec.ts.snap` | [View](setup-tailwind.spec.ts.snap_docs.md) | [View](setup-tailwind.spec.ts.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 332: packages/tailwind/src/utils/tailwindcss/tailwind-stylesheets


**Folder Path:** `packages/tailwind/src/utils/tailwindcss/tailwind-stylesheets`
**Generated:** 2025-11-15T20:38:38.043175Z

---

## Overview

This directory (`packages/tailwind/src/utils/tailwindcss/tailwind-stylesheets`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/tailwindcss/tailwind-stylesheets



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `preflight.ts` | [View](preflight.ts_docs.md) | [View](preflight.ts_kw.md) |
| `theme.ts` | [View](theme.ts_docs.md) | [View](theme.ts_kw.md) |
| `utilities.ts` | [View](utilities.ts_docs.md) | [View](utilities.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 333: packages/tailwind/src/utils/text


**Folder Path:** `packages/tailwind/src/utils/text`
**Generated:** 2025-11-15T20:38:38.046125Z

---

## Overview

This directory (`packages/tailwind/src/utils/text`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tailwind/src/utils/text



| File | Documentation | Keywords |
|------|---------------|----------|
| `from-dash-case-to-camel-case.ts` | [View](from-dash-case-to-camel-case.ts_docs.md) | [View](from-dash-case-to-camel-case.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 334: packages/text


**Folder Path:** `packages/text`
**Generated:** 2025-11-15T20:38:38.047064Z

---

## Overview

This directory (`packages/text`) contains a Node.js package. source code in the `src/` subdirectory. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `src/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/text



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `license.md` | [View](license.md_docs.md) | [View](license.md_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `readme.md` | [View](readme.md_docs.md) | [View](readme.md_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 335: packages/text/src


**Folder Path:** `packages/text/src`
**Generated:** 2025-11-15T20:38:38.049214Z

---

## Overview

This directory (`packages/text/src`) contains 

## Structure

- **Subdirectories:** 2
- **Documentation Files:** 3
- **Keyword Files:** 3

### Subdirectories

- `__snapshots__/`
- `utils/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/text/src



| File | Documentation | Keywords |
|------|---------------|----------|
| `index.ts` | [View](index.ts_docs.md) | [View](index.ts_kw.md) |
| `text.spec.tsx` | [View](text.spec.tsx_docs.md) | [View](text.spec.tsx_kw.md) |
| `text.tsx` | [View](text.tsx_docs.md) | [View](text.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 336: packages/text/src/__snapshots__


**Folder Path:** `packages/text/src/__snapshots__`
**Generated:** 2025-11-15T20:38:38.050655Z

---

## Overview

This directory (`packages/text/src/__snapshots__`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 1
- **Keyword Files:** 1

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/text/src/__snapshots__



| File | Documentation | Keywords |
|------|---------------|----------|
| `text.spec.tsx.snap` | [View](text.spec.tsx.snap_docs.md) | [View](text.spec.tsx.snap_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 337: packages/text/src/utils


**Folder Path:** `packages/text/src/utils`
**Generated:** 2025-11-15T20:38:38.051671Z

---

## Overview

This directory (`packages/text/src/utils`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This is a source code directory containing the implementation files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/text/src/utils



| File | Documentation | Keywords |
|------|---------------|----------|
| `compute-margins.spec.ts` | [View](compute-margins.spec.ts_docs.md) | [View](compute-margins.spec.ts_kw.md) |
| `compute-margins.ts` | [View](compute-margins.ts_docs.md) | [View](compute-margins.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 338: packages/tsconfig


**Folder Path:** `packages/tsconfig`
**Generated:** 2025-11-15T20:38:38.053132Z

---

## Overview

This directory (`packages/tsconfig`) contains a Node.js package. 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 4
- **Keyword Files:** 4

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains configuration files.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in packages/tsconfig



| File | Documentation | Keywords |
|------|---------------|----------|
| `base.json` | [View](base.json_docs.md) | [View](base.json_kw.md) |
| `nextjs.json` | [View](nextjs.json_docs.md) | [View](nextjs.json_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `react-library.json` | [View](react-library.json_docs.md) | [View](react-library.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 339: playground


**Folder Path:** `playground`
**Generated:** 2025-11-15T20:38:38.054766Z

---

## Overview

This directory (`playground`) contains a Node.js package. 

## Structure

- **Subdirectories:** 1
- **Documentation Files:** 5
- **Keyword Files:** 5

### Subdirectories

- `emails/`

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in playground



| File | Documentation | Keywords |
|------|---------------|----------|
| `CHANGELOG.md` | [View](CHANGELOG.md_docs.md) | [View](CHANGELOG.md_kw.md) |
| `README.md` | [View](README.md_docs.md) | [View](README.md_kw.md) |
| `components.ts` | [View](components.ts_docs.md) | [View](components.ts_kw.md) |
| `package.json` | [View](package.json_docs.md) | [View](package.json_kw.md) |
| `tsconfig.json` | [View](tsconfig.json_docs.md) | [View](tsconfig.json_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 340: playground/emails


**Folder Path:** `playground/emails`
**Generated:** 2025-11-15T20:38:38.056577Z

---

## Overview

This directory (`playground/emails`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in playground/emails



| File | Documentation | Keywords |
|------|---------------|----------|
| `.gitignore` | [View](.gitignore_docs.md) | [View](.gitignore_kw.md) |
| `example.tsx` | [View](example.tsx_docs.md) | [View](example.tsx_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

# Chapter 341: scripts


**Folder Path:** `scripts`
**Generated:** 2025-11-15T20:38:38.057847Z

---

## Overview

This directory (`scripts`) contains 

## Structure

- **Subdirectories:** 0
- **Documentation Files:** 2
- **Keyword Files:** 2

## Purpose & Concepts

*This section provides narrative context about the role and architecture of this directory.*

This directory contains build scripts and automation tools.

---

*For detailed file-by-file analysis, see the individual documentation files linked in the index.*



### Files in scripts



| File | Documentation | Keywords |
|------|---------------|----------|
| `check-dependency-versions.ts` | [View](check-dependency-versions.ts_docs.md) | [View](check-dependency-versions.ts_kw.md) |
| `pull-request-title-check.ts` | [View](pull-request-title-check.ts_docs.md) | [View](pull-request-title-check.ts_kw.md) |

---

## Navigation

- [↑ Parent Directory](../index.md)
- [📚 Documentation Overview](doc.md)
- [🔍 Keywords Index](sub.md)
- [🏠 Root Index](../index.md)

---

