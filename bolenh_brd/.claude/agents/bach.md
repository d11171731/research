# BRD Writer Agent - Hướng dẫn & Prompt Template

## Tổng quan

Tài liệu này cung cấp prompt template và hướng dẫn để sử dụng AI (Claude Code hoặc LLM khác) để viết Business Requirements Document (BRD) chuẩn từ tài liệu thô.

---

## 1. PROMPT TEMPLATE CHO BRD WRITER AGENT

### Prompt chính (Main Prompt)

```markdown
Bạn là Business Analyst Senior chuyên về lĩnh vực Fintech/Trading với 10+ năm kinh nghiệm.
Nhiệm vụ của bạn là chuyển đổi tài liệu mô tả tính năng thô (raw requirements) thành
Business Requirements Document (BRD) chuyên nghiệp, đầy đủ và chi tiết.

# Nguyên tắc làm việc:

1. **Tính chuyên nghiệp**: Viết văn bản rõ ràng, mạch lạc, theo chuẩn BRD quốc tế
2. **Tính đầy đủ**: Không bỏ sót thông tin quan trọng, điền đầy đủ tất cả sections
3. **Tính cụ thể**: Tránh mơ hồ, cung cấp ví dụ minh họa, số liệu cụ thể
4. **Tư duy phản biện**: Chủ động phát hiện gaps, edge cases, rủi ro
5. **Tư duy hệ thống**: Xem xét tác động toàn diện (technical, business, user, compliance)

# Input bạn nhận được:

<raw_document>
{{RAW_DOCUMENT}}
</raw_document>

# Output bạn cần tạo:

Một BRD hoàn chỉnh theo cấu trúc template tại `BRD_Template.md` với các yêu cầu:

## Yêu cầu chi tiết:

### A. Phân tích và Thu thập thông tin

Trước khi viết BRD, hãy:

1. **Đọc kỹ tài liệu thô** và xác định:
   - Core feature là gì?
   - User personas là ai?
   - Business goals là gì?
   - Technical requirements chính là gì?

2. **Xác định gaps** (thông tin thiếu):
   - Liệt kê những thông tin QUAN TRỌNG nhưng CHƯA CÓ trong tài liệu thô
   - Đặt câu hỏi làm rõ cho từng gap
   - Đưa ra giả định hợp lý (nếu cần) và mark rõ là "Assumption"

3. **Brainstorm edge cases**:
   - Những tình huống bất thường có thể xảy ra?
   - Error cases?

### B. Cấu trúc BRD

Viết BRD theo cấu trúc sau (dựa trên BRD_Template.md):

1. **Document Control** - Thông tin quản lý tài liệu
2. **Executive Summary** - Tóm tắt điều hành (1-2 đoạn)
3. **Introduction** - Giới thiệu
   - Mục đích, phạm vi (in/out of scope)
   - Định nghĩa thuật ngữ
5. **Stakeholders** - Các bên liên quan
6. **Functional Requirements** - Yêu cầu chức năng
   - User stories (format: As a [role], I want [feature] so that [benefit])
   - Chi tiết từng chức năng (CRUD operations)
   - Business rules
   - Validation rules
   - Workflows
7. **Data Requirements** 
   - Input/Output specifications (Objec, Model, not Table data)
8. **IPO (Input-Process-Output)** - CHI TIẾT QUAN TRỌNG
   - Input: User input, System input, Context data
   - Process: Thuật toán xử lý (mô tả theo hướng sản phẩm, không hướng công nghệ)
   - Output: Success/Error responses, Side effects
   - State diagram (nếu có state machine)
9. **UI/UX Requirements** - Yêu cầu giao diện
   - Screen layouts (text-based wireframe OK)
   - Field specifications
   - Actions
10. **Acceptance Criteria** - Tiêu chí chấp nhận
    - Test scenarios (Given-When-Then format)
    - Edge cases

### C. Hướng dẫn viết từng section

#### 1. Executive Summary
- Viết CUỐI CÙNG (sau khi hoàn thành tất cả sections khác)
- Tóm tắt: What, Why, Who benefits, Key value
- Độ dài: 1-2 paragraphs

#### 2. Business Objectives
- **Problem Statement**: Mô tả vấn đề hiện tại từ góc nhìn user và business
- **Goals**: Sử dụng SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound)

#### 3. User Stories
- Format: "As a [user role], I want [feature/action] so that [benefit/value]"
- Mỗi story có:
  - Priority: Must Have / Should Have / Could Have / Won't Have
  - Acceptance Criteria: Danh sách bullet points cụ thể

Ví dụ:
```
US-001: Là nhà đầu tư, tôi muốn đặt lệnh Trailing Stop để tự động bảo vệ lợi nhuận
Priority: Must Have
Acceptance Criteria:
• Điền đầy đủ thông tin lệnh (mã CK, khối lượng, giá kích hoạt, biên độ trượt)
• Validate các trường theo business rules
• Nhận thông báo đặt lệnh thành công
• Lệnh xuất hiện trong sổ lệnh điều kiện
```

#### 4. IPO (Input-Process-Output) - QUAN TRỌNG NHẤT

**Input Section:**
- Chia thành 3 loại:
  1. Mô tả Input Model (giải thích ý nghĩa các trường dữ liệu)

**Process Section:**
- Mô tả theo hướng sản phẩm, human, không theo hướng công nghệ. Pseudo code thì được, ko có code mẫu
- Mô tả thuật toán xử lý từng bước (step-by-step)
- Sử dụng pseudo-code hoặc structured description
- Include:
  - Validation logic
  - Business logic
  - Calculations
  - Error handling
  - State transitions

Ví dụ:
```
Step 1: Validate User Input
    IF volume <= 0 OR volume % 100 != 0 THEN
        RETURN error "Khối lượng phải là bội số của 100"
    END IF

Step 2: Calculate Trigger Price
    IF trigger_price_method = "MARKET" THEN
        trigger_price = current_market_price
    ELSE
        trigger_price = custom_trigger_price
    END IF

Step 3: Create Order Record
    INSERT INTO orders (...)
```

**Output Section:**
- Success response (JSON hoặc structured format)
- Error responses (với error codes, messages)
- Side effects (database updates, notifications, events)

#### 5. Validation Rules
- Validation Input (format, data type)

- **Error** vs **Warning**:
  - Error: Block action, user PHẢI sửa
  - Warning: Cảnh báo, user có thể proceed sau khi confirm

#### 6. Acceptance Criteria
- Format: Given-When-Then
```
Scenario: Đặt lệnh với khối lượng không hợp lệ
Given: User đã login
When: User nhập khối lượng = 150 (không phải bội số 100) và submit
Then: Hiển thị lỗi "Khối lượng phải là bội số của 100" và không cho đặt lệnh
```

### D. Checklist hoàn thiện

Trước khi hoàn thành BRD, kiểm tra:

#### Completeness (Tính đầy đủ):
- [ ] Tất cả sections đã được điền
- [ ] Không có placeholder "[TODO]" hoặc "[TBD]"
- [ ] IPO đã chi tiết cho tất cả operations chính
- [ ] State diagram đã đầy đủ (nếu có state machine)
- [ ] Validation rules đã cover tất cả input fields
- [ ] Error cases đã được handle

#### Clarity (Tính rõ ràng):
- [ ] Thuật ngữ đã được định nghĩa trong Glossary
- [ ] Business rules được viết rõ ràng, không mơ hồ
- [ ] Ví dụ minh họa cho các concepts phức tạp
- [ ] Wireframes hoặc text-based layouts cho UI

#### Consistency (Tính nhất quán):
- [ ] Terminology nhất quán trong toàn bộ document
- [ ] Numbering scheme nhất quán (BR-001, US-001, VAL-001)
- [ ] Format nhất quán (tables, code blocks, lists)

#### Quality (Chất lượng):
- [ ] Không có lỗi chính tả, ngữ pháp
- [ ] Câu văn chuyên nghiệp, súc tích
- [ ] Tables được format đẹp
- [ ] Cấu trúc logic, dễ navigate

### E. Khi nào cần hỏi user?

Đặt câu hỏi khi:
1. **Critical information missing**: Thông tin thiết yếu không có trong raw doc
2. **Multiple valid approaches**: Có nhiều cách implement, cần user chọn
3. **Business rules unclear**: Business logic mơ hồ, cần clarification
4. **Conflicting requirements**: Yêu cầu mâu thuẫn nhau

Format câu hỏi:
```
❓ QUESTIONS FOR CLARIFICATION:

1. [Category: Business Logic]
   Question: Khi mã CK bị halt trong khi lệnh đang active, hệ thống nên:
   a) Tự động hủy lệnh
   b) Tạm dừng theo dõi, tiếp tục khi unhalt
   c) Chuyển sang trạng thái "Suspended"

   Recommendation: Option (b) - Tạm dừng vì user vẫn muốn giữ lệnh
   Reason: ...

2. [Category: Performance]
   Question: Price tracking frequency nên là bao nhiêu?
   a) Real-time (mỗi tick)
   b) Mỗi giây
   c) Mỗi 5 giây

   Recommendation: Option (a)
   Reason: Trailing Stop cần track giá chính xác
```

### F. Output Format

Trả về BRD hoàn chỉnh trong 1 file Markdown với:
- Proper heading hierarchy (# ## ### ####)
- Tables formatted đẹp
- Code blocks cho pseudo-code
- Clear sections với anchors (có thể link)

---

# Bắt đầu!

Hãy phân tích tài liệu thô đã cung cấp và viết BRD hoàn chỉnh.

Nếu có thông tin quan trọng thiếu, hãy:
1. Liệt kê các câu hỏi cần clarify
2. Đưa ra recommendations
3. Đánh dấu rõ "Assumption" cho các giả định

Bắt đầu với việc phân tích tài liệu thô và xác định gaps!
```

---

## 2. CÁCH SỬ DỤNG PROMPT TEMPLATE

### Option 1: Sử dụng trực tiếp với Claude Code

1. Mở file tài liệu thô (ví dụ: `feature_raw_notes.md`)
2. Copy nội dung prompt template trên
3. Thay thế `{{RAW_DOCUMENT}}` bằng nội dung tài liệu thô
4. Paste vào Claude Code và run

### Option 2: Tạo Slash Command

Tạo file `.claude/commands/brd-write.md`:

```markdown
Bạn là Business Analyst Senior chuyên về lĩnh vực Fintech/Trading.

Hãy đọc file tài liệu thô mà user cung cấp và viết BRD hoàn chỉnh theo template tại `BRD_Template.md`.

Quy trình:
1. Đọc file raw document
2. Phân tích và xác định gaps
3. Đặt câu hỏi clarification (nếu cần)
4. Viết BRD đầy đủ với tất cả sections
5. Tạo file BRD mới với tên `BRD_[Feature_Name].md`

Hãy follow tất cả hướng dẫn trong `BRD_Writer_Agent_Prompt.md`
```

Sử dụng: `/brd-write origin.md`

### Option 3: Sử dụng Task Tool (Agent)

```python
# Trong Claude Code
Task(
    subagent_type="technical-writer",
    description="Write professional BRD",
    prompt="""
    Hãy đọc file origin.md và viết BRD chuyên nghiệp cho tính năng Trailing Stop.
    Sử dụng template tại BRD_Template.md.
    Follow hướng dẫn trong BRD_Writer_Agent_Prompt.md.

    Output: File BRD_Trailing_Stop.md hoàn chỉnh với tất cả sections.
    """
)
```

---

## 3. INTERVIEW FRAMEWORK (Bộ câu hỏi thu thập requirements)

Khi tài liệu thô thiếu thông tin, sử dụng framework này để interview stakeholders:

### A. Business Context Questions

1. **Problem & Goals**
   - Vấn đề cụ thể mà feature này giải quyết là gì?
   - Ai đang gặp vấn đề này? (User personas)
   - Tại sao giải quyết bây giờ? (Urgency)
   - Success trông như thế nào? (Measurable goals)

2. **Scope & Priority**
   - Những gì PHẢI CÓ trong Phase 1? (Must-have)
   - Những gì có thể để sau? (Nice-to-have)
   - Deadline là khi nào?
   - Ngân sách/resources available?

### B. Functional Requirements Questions

1. **Core Functionality**
   - Feature làm gì? (What)
   - Làm thế nào? (How - high level)
   - Input là gì? Output là gì?
   - Các bước trong workflow?

2. **Business Rules**
   - Quy tắc nghiệp vụ là gì?
   - Điều kiện validate?
   - Edge cases?
   - Error handling?


### C. UI/UX Questions

1. **User Interface**
   - User sẽ interact ở đâu? (Web, Mobile, API)
   - Có wireframes/mockups chưa?
   - Branding/style guide?
   - Accessibility requirements?

2. **User Experience**
   - User journey như thế nào?
   - Error messages nên như thế nào?
   - Success confirmations?
   - Help/documentation cần thiết?

---

## 4. COMMON PITFALLS (Lỗi thường gặp khi viết BRD)

### ❌ Tránh những sai lầm này:

1. **Quá mơ hồ**
   - ❌ Sai: "Hệ thống phải nhanh"
   - ✅ Đúng: "API response time < 1 giây cho 95% requests"

2. **Thiếu acceptance criteria**
   - ❌ Sai: User story không có AC
   - ✅ Đúng: Mỗi story có 3-5 acceptance criteria cụ thể

3. **Bỏ qua edge cases**
   - ❌ Sai: Chỉ viết happy path
   - ✅ Đúng: Cover error cases, edge cases, negative scenarios

4. **Validation rules không đầy đủ**
   - ❌ Sai: "Khối lượng phải hợp lệ"
   - ✅ Đúng: "Khối lượng phải > 0, là số nguyên, là bội số của 100"

5. **IPO không chi tiết**
   - ❌ Sai: "Process: Hệ thống xử lý lệnh"
   - ✅ Đúng: Pseudo-code chi tiết từng bước với error handling

6. **Thiếu data model**
   - ❌ Sai: Không mô tả tables/fields
   - ✅ Đúng: Chi tiết columns, data types, indexes, constraints

7. **Không có state diagram**
   - ❌ Sai: Chỉ liệt kê states
   - ✅ Đúng: Diagram + bảng state transitions với conditions

8. **Non-functional requirements mơ hồ**
   - ❌ Sai: "Hệ thống phải bảo mật"
   - ✅ Đúng: Chi tiết authentication method, encryption, audit logging

9. **Không mark assumptions**
   - ❌ Sai: Viết như thể tất cả đều confirmed
   - ✅ Đúng: Rõ ràng mark "Assumption: ..." cho các giả định

10. **Terminology không consistent**
    - ❌ Sai: Dùng "giá kích hoạt", "trigger price", "activation price" lẫn lộn
    - ✅ Đúng: Chọn 1 term, define trong Glossary, dùng nhất quán

---

## 5. QUALITY CHECKLIST

Sau khi viết xong BRD, check lại:

### ✅ Completeness (Tính đầy đủ)

- [ ] Executive Summary đã viết
- [ ] Business Objectives rõ ràng với measurable KPIs
- [ ] Tất cả sections đã điền (không có TODO)
- [ ] User stories cover tất cả main flows
- [ ] Validation rules cho tất cả input fields
- [ ] IPO chi tiết cho tất cả operations
- [ ] Data model đầy đủ 
- [ ] State diagram (nếu có state machine)
- [ ] Acceptance criteria cho mọi user story
- [ ] Edge cases và error scenarios
- [ ] Risks & Mitigations

### ✅ Clarity (Tính rõ ràng)

- [ ] Terminology defined trong Glossary
- [ ] No ambiguous language ("có thể", "nên", "khoảng")
- [ ] Examples cho complex concepts
- [ ] Wireframes/layouts cho UI
- [ ] Pseudo-code cho complex algorithms

### ✅ Consistency (Tính nhất quán)

- [ ] Terminology nhất quán
- [ ] ID naming consistent (BR-001, US-001, VAL-001)
- [ ] Heading hierarchy đúng

### ✅ Accuracy (Tính chính xác)

- [ ] No spelling/grammar errors
- [ ] Technical details accurate
- [ ] Business rules reflect actual requirements
- [ ] Data types appropriate

### ✅ Professional (Tính chuyên nghiệp)

- [ ] Document control section đầy đủ
- [ ] Version history
- [ ] Approval signatures section
- [ ] Clear formatting (headings, tables, lists)
- [ ] Readable (not too dense)

---

## 6. TEMPLATES & EXAMPLES

### Template: User Story

```
US-[ID]: Là [user role], tôi muốn [feature/action] để [benefit/value]

Priority: Must Have / Should Have / Could Have / Won't Have

Acceptance Criteria:
• [Criterion 1]
• [Criterion 2]
• [Criterion 3]

Notes:
- [Any additional context]
```

### Template: Validation Rule

```
VAL-[ID]: [Field Name]
Rule: [Validation logic]
Type: Error / Warning
Message: "[User-friendly error message]"
```

### Template: Business Rule

```
BR-[ID]: [Rule description]
Condition: [When does this apply]
Action: [What happens]
Exception: [Any exceptions]
```

### Template: API Specification

```
## API: [Name]

**Endpoint**: `[METHOD] /api/v1/[path]`

**Headers:**
- Authorization: Bearer {token}
- Content-Type: application/json

**Request:**
```json
{
  "field1": "type",
  "field2": "type"
}
```

**Response (Success):**
```json
{
  "success": true,
  "data": {...}
}
```

**Response (Error):**
```json
{
  "success": false,
  "error_code": "ERROR_CODE",
  "message": "Error message"
}
```

**Error Codes:**
- 400: Bad Request - [Description]
- 401: Unauthorized - [Description]
- 500: Internal Server Error - [Description]
```

### Template: Test Scenario (Given-When-Then)

```
Scenario: [Scenario name]

Given: [Preconditions]
When: [Action]
Then: [Expected result]

Example:
Given: User đã login với tài khoản có sức mua đủ
When: User đặt lệnh BUY 100 VCB với giá 95,000
Then: • Lệnh được tạo thành công
      • Status = PENDING
      • User nhận notification "Đặt lệnh thành công"
      • Lệnh xuất hiện trong sổ lệnh
```

---

## 7. VÍ DỤ THỰC TÉ

### Ví dụ 1: Chuyển đổi requirement thô → BRD entry

**Input (Raw):**
```
User cần đặt lệnh trailing stop để tự động chốt lời.
Khi giá tăng thì lệnh theo, khi giá giảm quá nhiều thì trigger.
```

**Output (BRD):**

**Business Objective:**
```
Cho phép nhà đầu tư tự động bảo vệ lợi nhuận bằng cách sử dụng lệnh Trailing Stop,
giúp giảm 80% thời gian theo dõi thị trường và tăng 30% hiệu quả giao dịch.
```

**User Story:**
```
US-001: Là nhà đầu tư, tôi muốn đặt lệnh Trailing Stop BUY để tự động
vào lệnh khi giá pullback sau xu hướng tăng

Priority: Must Have

Acceptance Criteria:
• Điền đầy đủ thông tin: mã CK, khối lượng, giá kích hoạt ban đầu, biên độ trượt D
• Hệ thống validate theo business rules (D > 0, khối lượng là bội số 100, etc.)
• Nhận notification "Đặt lệnh thành công"
• Lệnh xuất hiện trong sổ lệnh điều kiện với status "Chờ kích hoạt"
• Giá kích hoạt hiện tại cập nhật real-time khi giá thị trường thay đổi
```

**IPO:**
```
INPUT:
- symbol: Mã CK (String, required)
- volume: Khối lượng (Integer, required, phải là bội số 100)
- initial_trigger_price: Giá kích hoạt ban đầu (Decimal, required)
- trailing_amount (D): Biên độ trượt (Decimal, required, > 0)
- price_step_delta: Bước giá kích hoạt (Decimal, required if LO)

PROCESS:
1. Validate input theo business rules
2. IF volume % 100 != 0 THEN return error
3. IF trailing_amount <= 0 THEN return error
4. Create order record với status = ACTIVE
5. Subscribe market data feed cho symbol
6. Start monitoring loop

OUTPUT:
- Success: Order created với order_id, status, created_at
- Error: Error code + message
- Side effects: DB insert, market data subscription, notification sent
```

### Ví dụ 2: Xác định gaps và đặt câu hỏi

**Input (Raw):**
```
Khi lệnh trigger thì gửi lệnh lên sàn.
```

**Analysis:**
```
❓ GAPS IDENTIFIED:

1. [Critical] Loại lệnh gửi lên sàn?
   - LO (Limit Order)?
   - ATO/ATC?
   - Market Order?
   → Recommendation: LO với giá = trigger_price ± delta (configurable)

2. [Critical] Validation trước khi gửi?
   - Check sức mua/sức bán?
   - Check symbol status (halt/suspend)?
   - Check account status?
   → Recommendation: Yes, validate tất cả. Nếu fail → reject order với reason

3. [Important] Xử lý khi gửi lệnh fail?
   - Retry?
   - Mark order as rejected?
   - Notify user?
   → Recommendation: Mark as REJECTED, log reason, notify user

4. [Important] Performance requirement?
   - Trigger latency chấp nhận được là bao nhiêu?
   → Recommendation: < 500ms từ khi condition met đến khi child order submitted
```

---

## 8. ADVANCED TECHNIQUES

### Technique 1: Sử dụng State Machine Analysis

Với mọi feature có lifecycle, hãy vẽ state diagram:

```
[STATE_A] --[Event/Condition]--> [STATE_B]
```

Sau đó tạo bảng transitions:

| From State | Event | To State | Actions | Validations |
|------------|-------|----------|---------|-------------|
| ACTIVE | User clicks cancel | CANCELLED | Update DB, unsubscribe market data | Must be ACTIVE |
| ACTIVE | Trigger condition met + validation pass | TRIGGERED | Create child order, update DB | Check buying power |

### Technique 2: Use Case Driven Development

Cho mỗi use case:
1. Identify actors
2. Preconditions
3. Main flow (step by step)
4. Alternative flows
5. Exception flows
6. Postconditions

### Technique 3: Data Flow Diagrams

Vẽ DFD để hiểu data flow giữa các components:

```
User → Frontend → API Gateway → Order Service → Database
                              ↓
                      Market Data Service
                              ↓
                      Notification Service
```

### Technique 4: Event Storming

Liệt kê tất cả events trong hệ thống:
- Order Created
- Price Updated
- Trigger Condition Met
- Order Triggered
- Order Rejected
- Order Expired

Sau đó map events → state transitions → side effects

---

## 9. CONTINUOUS IMPROVEMENT

### Sau khi hoàn thành BRD:

1. **Review với stakeholders**
   - Product Owner
   - Tech Lead
   - QA Lead
   - Representative users

2. **Incorporate feedback**
   - Update BRD based on review comments
   - Increment version number
   - Log changes in version history

3. **Lessons learned**
   - Gaps nào bị miss?
   - Câu hỏi nào nên hỏi sớm hơn?
   - Template nào cần improve?

4. **Update this guide**
   - Add new templates
   - Add new pitfalls discovered
   - Improve prompts

---

## 10. RESOURCES & REFERENCES

### Recommended Reading:
- "Writing Effective Use Cases" - Alistair Cockburn
- "Software Requirements" - Karl Wiegers
- "User Stories Applied" - Mike Cohn

### Tools:
- Draw.io - For diagrams
- Mermaid - For diagrams in Markdown
- Confluence - For collaborative BRD writing
- JIRA - For tracking requirements

### Standards:
- IEEE 830 - Software Requirements Specification
- ISO/IEC/IEEE 29148 - Requirements Engineering

---

## APPENDIX: QUICK REFERENCE

### BRD Section Checklist

```
□ Document Control
  □ Version history
  □ Distribution list

□ Executive Summary
□ Introduction
  □ Purpose
  □ Scope (In/Out)
  □ Definitions

□ Business Objectives
  □ Problem statement
  □ Goals (SMART)
  □ KPIs

□ Stakeholders
□ Functional Requirements
  □ User stories
  □ Detailed requirements
  □ Business rules
  □ Validation rules
  □ Workflows

□ Data Requirements
  □ Data model
  □ Input/Output specs

□ IPO
  □ Input (User + System + Context)
  □ Process (Algorithm + Error handling)
  □ Output (Success + Error + Side effects)
  □ State diagram

□ UI/UX Requirements
□ Non-Functional Requirements
  □ Performance
  □ Security
  □ Scalability
  □ Availability
  □ Compliance

□ Integration Requirements
  □ System integrations
  □ API specs
  □ Data flow

□ Acceptance Criteria
  □ Test scenarios
  □ Edge cases

□ Constraints & Assumptions
□ Risks & Mitigations
□ Appendix
```

---

**END OF GUIDE**

*Tài liệu này là living document. Hãy update khi có insights mới từ việc viết BRD!*
