# Source of truth for the portfolio page. Edit and run: python3 build.py
FLAGSHIP = [
  ("ai-receipt-tracker", "Flagship monorepo: Next.js web app, Flutter mobile app and a TypeScript API with auth, Stripe in test mode and LLM receipt extraction (mock provider by default).", "https://applycoding.github.io/ai-receipt-tracker/"),
  ("ros2-voice-command-robot", "ROS2 robot driven by voice: VAD, speech-to-text and local LLM intent parsing turn spoken commands into Nav2 goals in a Gazebo world. Mock backends in CI.", None),
]
GROUPS = {
 "AI and LLM systems": [
  "agent-guardrails-observability","llm-serving-finetune-lab","multi-agent-langgraph-workflow","mcp-jira-github-server",
  "llm-rag-api","llm-eval-observability","rag-llm-eval-demo","document-ai-extraction","lora-finetune-small-llm",
  "offline-voice-assistant","azure-openai-functions-bot","gcp-vertex-ai-agent","search-ranking-recsys"],
 "Mobile (Flutter, Android, iOS)": [
  "flutter-offline-first-app","flutter-on-device-ml","flutter-ble-health-tracker","flutter-ride-booking-demo",
  "kotlin-ble-iot-companion","android-mvvm-retrofit-app","kmp-compose-swiftui-pos","ios-swiftui-app"],
 "Full stack and cloud": [
  "nextjs-saas-dashboard","react-ts-fleet-dashboard","angular-admin-portal","laravel-vue-saas-starter","payments-stripe-api",
  "vat-tax-ledger-engine","realtime-chat-backend","graphql-federation-gateway","fullstack-graphql-grpc-demo",
  "go-grpc-inventory-service","go-ride-dispatch","springboot-banking-ledger-api","spring-boot-wallet-api",
  "dotnet-blazor-admin-portal","dotnet-ride-booking-api","aws-serverless-api","terraform-multicloud-api",
  "k8s-microservice-deploy","jenkins-gitops-pipeline","opentelemetry-tracing-demo","camunda-bpmn-order-workflow",
  "kotlin-growth-experiments-service","crypto-custody-signer","cpp-vectorized-query-engine","system-design-case-studies"],
 "Robotics, drones and edge AI": [
  "ros2-nav2-slam-sim","px4-drone-mission-planner","ros2-drone-mission-sim","ros2-vision-tracking-demo",
  "robot-fleet-mqtt-telemetry","robot-learning-vla-demo","edge-yolo-tensorrt","edge-vision-detector","cpp-flight-controller",
  "humanoid-edge-ai-gps-denied-sim","firefighter-multimodal-edge-ai-sim"],
}
# Live demos (GitHub Pages). Add repo -> URL as they go live.
LIVE = {
  "react-ts-fleet-dashboard": "https://applycoding.github.io/react-ts-fleet-dashboard/",
  "angular-admin-portal": "https://applycoding.github.io/angular-admin-portal/",
}
# Fallback descriptions for repos without a GitHub description.
DESC = {
  "angular-admin-portal": "Angular admin portal (Harborline): route guard and HTTP interceptor auth, NgRx entity store, server-style paging, English and Spanish i18n.",
  "aws-serverless-api": "Serverless reservation API: Cognito JWT, API Gateway HTTP API, Python Lambda, DynamoDB single table, SQS worker and EventBridge expiry.",
  "azure-openai-functions-bot": "Python Azure Functions support assistant on Azure OpenAI with tool calling (order lookup, ticket creation) and Bicep infrastructure.",
  "camunda-bpmn-order-workflow": "Camunda 8 (Zeebe) order approval process with Spring Boot job workers and a DMN decision table.",
  "dotnet-blazor-admin-portal": ".NET 8 Blazor admin portal (Meridian Desk) with role-based sign-in, customers, orders, tickets and a minimal API layer.",
  "flutter-offline-first-app": "Flutter offline-first inspection checklists: Drift (SQLite) storage and a sync queue that pushes when back online.",
  "flutter-on-device-ml": "Flutter on-device object detection (TensorFlow Lite) and text recognition (ML Kit); photos never leave the phone.",
  "flutter-ride-booking-demo": "Flutter rider app on OpenStreetMap with fares and a simulated driver, backed by a Cloudflare Workers API with D1 and Durable Objects.",
  "fullstack-graphql-grpc-demo": "Hotel desk demo: React client, GraphQL gateway and a gRPC booking service.",
  "gcp-vertex-ai-agent": "Python support agent on Gemini (Vertex AI) with tool calling, FastAPI, Cloud Run and Firestore targets; offline mode by default.",
  "go-grpc-inventory-service": "Go inventory service with idempotent stock reservations, serving gRPC and a gRPC-Gateway REST API.",
  "graphql-federation-gateway": "Apollo Federation 2 gateway over two TypeScript subgraphs with JWT checks and query depth and complexity limits.",
  "jenkins-gitops-pipeline": "Jenkins pipeline that promotes a Python service through Kustomize overlays, with Argo CD manifests.",
  "kotlin-ble-iot-companion": "Kotlin Android BLE sensor companion: scan, connect, decode notifications, live charts, Room storage, CSV export.",
  "laravel-vue-saas-starter": "Multi-tenant SaaS starter (Keel): Laravel 11, Vue 3, Inertia, Tailwind, team roles enforced with policies.",
  "lora-finetune-small-llm": "LoRA supervised fine-tuning pipeline (transformers, peft, trl) that turns maintenance logs into structured JSON.",
  "nextjs-saas-dashboard": "Next.js SaaS analytics dashboard (Signalboard) with organisations, projects, events, role-based access and charts.",
  "opentelemetry-tracing-demo": "Three-service checkout flow emitting OpenTelemetry traces, metrics and logs to Jaeger, Prometheus and Grafana.",
  "px4-drone-mission-planner": "PX4 survey-grid mission planner: polygon to lawnmower path, geofence and return-to-home energy checks, MAVSDK upload.",
  "rag-llm-eval-demo": "Retrieval-augmented QA service with local embeddings and an evaluation harness that runs without an API key.",
  "robot-learning-vla-demo": "Data-centric robot learning on a planar arm in simulation.",
  "ros2-nav2-slam-sim": "ROS 2 Humble indoor robot: Gazebo office world, slam_toolbox mapping, Nav2 and a YAML waypoint mission runner.",
  "ros2-vision-tracking-demo": "ROS 2 pipeline: YOLO detection plus a ByteTrack-style Kalman and IoU tracker, publishing annotated images.",
  "springboot-banking-ledger-api": "Spring Boot double-entry banking ledger with BigDecimal amounts and optimistic locking for concurrent transfers.",
  "system-design-case-studies": "System design notes: humanoid onboard stack, ride-hailing dispatch, POS, drone mission control, edge vision, agent platform.",
}
TOP6 = ["ai-receipt-tracker","agent-guardrails-observability","ros2-voice-command-robot","llm-serving-finetune-lab","kmp-compose-swiftui-pos","react-ts-fleet-dashboard"]
