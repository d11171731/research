# IPAM Framework - Organization Change Management

## 📚 Cấu Trúc Thư Mục

```
.ipam/
├── README.md                          # File này
├── docs/
│   ├── oc-complete-guide.md          # Hướng dẫn chi tiết đầy đủ
│   └── ipam-framework-summary.md     # Tóm tắt nhanh framework
├── templates/
│   └── oc-template.md                # Template OC document trống
├── tac/                               # TAC documents (IDENTIFY phase only)
│   └── (TAC documents sẽ được lưu ở đây)
└── ocs/                               # OC documents đầy đủ (4 phases)
    └── (OC documents sẽ được lưu ở đây)
```

---

## 🚀 Cách Sử dụng

### 1A. TAC - IDENTIFY Phase Only (Recommended để bắt đầu)

**Khi nào dùng:** Khi bạn cần hiểu sâu vấn đề trước khi lên plan chi tiết.

```bash
/tac
```

Command này sẽ:
- ✅ TAC Analysis: Transform, Amplify, Continue
- ✅ 5I Framework: Intention → Interconnect → Insight → Innovation → Integrity
- ✅ Hiển thị progress [1/5] → [5/5]
- ✅ Tự động lưu vào `.ipam/tac/TAC-{code}.md`

**Flow:**

```
User: /tac

Claude:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 TAC - Transform, Amplify, Continue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Tell me about the situation:
1. What problem are you trying to solve?
2. What's the current pain point?

User: [trả lời...]

Claude:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[TAC Analysis]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 TRANSFORM: What must fundamentally change?
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1/5] 💡 INTENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
...
```

**Output:** TAC document focused on problem understanding & solution options.

---

### 1B. Full OC Document (All 4 Phases)

**Khi nào dùng:** Khi bạn ready để lập full plan từ IDENTIFY → MANAGE.

```bash
/oc-create
```

Command này sẽ:
- ✅ Hỏi bạn từng câu theo IPAM framework (4 phases)
- ✅ Hiển thị progress [1/5] → [5/5] trên CLI
- ✅ Generate OC document đầy đủ
- ✅ Tự động lưu vào `.ipam/ocs/OC-{code}.md`

**Flow:**

```
User: /oc-create

Claude:
🎯 OC Creator - Let's build your Organization Change document

📝 First, tell me about the change:
1. What problem are you trying to solve?
2. What's the desired outcome?

User: [trả lời...]

Claude:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1/5] 🔍 IDENTIFY PHASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 INTENTION - Define Your Vision
...

[2/5] 📝 PLAN PHASE (OTOOB)
...

[3/5] ✅ ACCOUNTABILITY PHASE (OMVP)
...

[4/5] 📊 MANAGE PHASE
...
```

**Output:** Comprehensive OC document with all 4 phases.

---

### 💡 Nên dùng command nào?

| Scenario | Command | Why |
|----------|---------|-----|
| Chưa rõ vấn đề, cần explore | `/tac` | Focus vào IDENTIFY, không overwhelm |
| Đã clear problem, cần full plan | `/oc-create` | One-shot full planning |
| Quick assessment | `/tac` | Faster, lighter |
| Complete project planning | `/oc-create` | Comprehensive |

**Recommendation:** Bắt đầu với `/tac` để understand deeply, sau đó dùng insights để run `/oc-create` nếu cần full plan.

### 2. Tạo Document Thủ Công

Copy template:

```bash
cp .ipam/templates/oc-template.md .ipam/ocs/OC-YOUR-CODE.md
```

Sau đó điền thông tin vào template.

### 3. Tham Khảo Documentation

**Quick Reference (5 phút):**
```bash
cat .ipam/docs/ipam-framework-summary.md
```

**Full Guide (30-60 phút):**
```bash
cat .ipam/docs/oc-complete-guide.md
```

Hoặc mở trong editor:
```bash
open .ipam/docs/oc-complete-guide.md
```

---

## 📖 IPAM Framework Tóm Tắt

### 4 Phases

```
[1] IDENTIFY (5I)
    ↓ Transform, Amplify, Continue
[2] PLAN (5P - OTOOB)
    ↓ OC Owner + Timeframe + One Team + Outputs + Biz Impact
[3] ACCOUNTABILITY (5A - OMVP)
    ↓ Objective Minimum Viable Product
[4] MANAGE (5M)
    ↓ Sustainable Results
```

### Key Concepts

- **OTOOB**: OC Owner + Timeframe + One Team + Outputs + Biz Impact
- **OMVP**: Objective Minimum Viable Product (outcome-focused MVP)
- **5I**: Intention → Interconnect → Insight → Innovation → Integrity
- **5P**: Purpose → Pathway → Perspective → Priorities → Performance
- **5A**: Align → Assign → Action → Access → Adapt
- **5M**: Map → Measure → Monitor → Modify → Maintain

---

## 🎯 Khi Nào Dùng IPAM?

| Tình Huống | Phase Bắt Đầu |
|------------|----------------|
| Có ý tưởng mới, cần define rõ | IDENTIFY |
| Đã có vision, cần plan cụ thể | PLAN |
| Đã có plan, ready để execute | ACCOUNTABILITY |
| Đã launch, cần sustain & improve | MANAGE |

---

## 💡 Tips

1. **Luôn bắt đầu với customer objective**: Khách hàng cần gì? Outcome mong đợi?

2. **OMVP > MVP**: Focus vào outcome, không chỉ output. Minimum scope để deliver objective.

3. **Data-driven**: Luôn có baseline, target, và cách measure

4. **Iterate nhanh**: Không cần perfect, cần feedback sớm

5. **Document as you go**: Update OC document khi có thông tin mới

6. **Celebrate milestones**: Recognize team sau mỗi phase hoàn thành

---

## 📂 Conventions

### TAC Code Format (IDENTIFY phase only)

```
TAC-{YEAR}-{DEPT}-{NUM}

Examples:
- TAC-2025-CX-001   (Customer Experience TAC #1)
- TAC-2025-ENG-002  (Engineering TAC #2)
- TAC-2025-OPS-010  (Operations TAC #10)
```

### OC Code Format (Full 4 phases)

```
OC-{YEAR}-{DEPT}-{NUM}

Examples:
- OC-2025-CX-001   (Customer Experience OC #1)
- OC-2025-ENG-002  (Engineering OC #2)
- OC-2025-OPS-010  (Operations OC #10)
```

### File Naming

```
TAC documents: .ipam/tac/TAC-{CODE}.md
OC documents:  .ipam/ocs/OC-{CODE}.md

Examples:
- .ipam/tac/TAC-2025-CX-001.md
- .ipam/ocs/OC-2025-CX-001.md
```

### Status Values

- `Draft` - Đang soạn thảo
- `Planning` - IDENTIFY/PLAN phase
- `In Progress` - ACCOUNTABILITY phase (đang execute)
- `Completed` - Đã hoàn thành
- `On Hold` - Tạm dừng

---

## 🔧 Troubleshooting

### Q: Command `/tac` hoặc `/oc-create` không hoạt động?

**A:** Đảm bảo files tồn tại:
- `.claude/commands/tac.md`
- `.claude/commands/oc-create.md`

Reload Claude Code nếu cần.

### Q: Tôi có thể customize template không?

**A:** Có! Edit file `.ipam/templates/oc-template.md` theo nhu cầu.

### Q: OC document quá dài, có thể rút gọn không?

**A:** Có. Chỉ cần giữ các section thiết yếu cho context của bạn. Template là guide, không phải strict rule.

### Q: Tôi có thể dùng IPAM cho personal projects không?

**A:** Hoàn toàn! Scale down theo nhu cầu. Ví dụ: Không cần RACI matrix chi tiết nếu là solo project.

---

## 📞 Support

Đọc thêm:
- Full Guide: `.ipam/docs/oc-complete-guide.md`
- Quick Reference: `.ipam/docs/ipam-framework-summary.md`
- Template: `.ipam/templates/oc-template.md`

---

## 📝 Examples

Xem examples trong full guide:
```bash
less .ipam/docs/oc-complete-guide.md
```

Search for "Example:" để tìm các ví dụ cụ thể.

---

**Version:** 1.0
**Last Updated:** 2025-10-29
**Maintained by:** IPAM Framework Team
