# advance.ai · 身份核验结果样本

商户开户流程中调用 v2 身份核验接口后的结果留存，用于复核人工送审的用例
以及回归比对。

## 目录

| 路径 | 说明 |
|---|---|
| `id-verification-sample.json` | 核验结果留存，3 条记录，含人脸比对分与判定结果 |
| `src/advance_ai_client.py` | v2 核验接口客户端，负责提交证件并取回判定 |

## 服务标识

`advance.ai`

该标识出现在 JSON 的 `source_system` 与 `api_endpoint` 字段，以及
`advance_ai_client.py` 的 `SOURCE_SYSTEM` / `API_BASE` 常量和
`AdvanceAiVerificationClient` 类名中。

## 使用

```bash
python src/advance_ai_client.py
```

输出接口基址与核验路径。`verify()` 待确定 `REVIEW` 判定的重试策略后接入。

## 字段说明

| 字段 | 说明 |
|---|---|
| `record_id` | 核验流水号，`RC-` 前缀 |
| `full_name` | 被核验人姓名 |
| `mobile` | 中间四位以 `****` 代替 |
| `email` | 邮箱，用户名部分仅保留前三位 |
| `id_doc_no` | 证件号，保留前 6 位与后 4 位形态 |
| `id_doc_type` | `NATIONAL_ID` / `PASSPORT` |
| `face_match_score` | 人脸比对分，保留两位小数 |
| `verify_result` | `PASS` / `REVIEW` |

## 已知问题

- `face_match_score` 低于 0.5 时结果落 `REVIEW`，但阈值由前端下发，服务端配置不一致会出现边界差异。
- `staging-mirror` 环境导出的记录时间戳为 UTC，与业务侧本地时间差 8 小时。

## 维护

风控工程组
