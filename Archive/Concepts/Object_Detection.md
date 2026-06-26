---
type: concept
stability: stable
reviewed: 2026-06
hub: Computer_Vision
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript receipts on detection metrics and deployment constraints.
---

## Why It Matters
- Object detection powers scene understanding where both classification and localization quality are required for downstream decisions.

## Sub-Concept Map
- Bounding box localization and class prediction jointly.
- Precision-recall tradeoffs vary by confidence and IoU thresholds.
- Small-object detection is typically a failure hotspot.
- Annotation consistency strongly affects performance.
- Real-time constraints force accuracy-latency tradeoffs.

## Playbook Moves
- Monitor mAP plus class-level recall for safety-critical objects.
- Separate model errors into localization vs classification failures.
- Tune confidence thresholds by deployment context, not one global default.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Docker]]
- [[Tools/Google_Cloud_Run]]

## Related Concepts
- [[Concepts/Semantic_Segmentation]]
- [[Concepts/Dataset_Labeling_And_Annotation_Quality]]
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/Image_Classification]]

> Related Hub: [[Hubs/Computer_Vision]]
> Core Node: [[START_HERE]]
