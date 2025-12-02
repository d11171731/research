# HƯỚNG DẪN SỬ DỤNG GANTT CHART
## How to Use ITSM Roadmap Gantt Chart Files

---

## 📁 FILES ĐÃ TẠO (Generated Files)

1. **ITSM-Roadmap-Gantt-Chart.md** (655 KB)
   - Visual Gantt chart dạng text
   - Đọc trực tiếp trên GitHub, VS Code, hoặc bất kỳ markdown viewer
   - Có color coding, dependencies, resource loading

2. **ITSM-Roadmap-Gantt.csv** (15 KB)
   - CSV format chuẩn cho import
   - Tương thích Excel, MS Project, Google Sheets
   - 70+ tasks với full details

3. **HOW-TO-USE-GANTT-CHART.md** (file này)
   - Hướng dẫn sử dụng
   - Recommendations cho tools

---

## 🎯 OPTION 1: ĐỌC TRỰC TIẾP FILE MARKDOWN

### Cho ai?
- **Leadership muốn overview nhanh**
- **Team leads cần xem dependencies**
- **Stakeholders cần timeline visual**

### Cách dùng:
1. Mở file `ITSM-Roadmap-Gantt-Chart.md` bằng:
   - GitHub (đẹp nhất)
   - VS Code với Markdown Preview
   - Obsidian, Notion, hoặc bất kỳ markdown reader

2. Navigate theo sections:
   - **Q1-Q4 Timelines:** Xem visual timeline từng tháng
   - **Critical Path Analysis:** Hiểu dependencies chính
   - **Resource Loading:** Xem workload từng team
   - **Budget Timeline:** Track spending theo quarter
   - **OC1-OC4 Progress:** Track objective completion

### Advantages:
✅ Không cần tool gì
✅ Color coded rõ ràng
✅ Dependencies visualization tốt
✅ Resource & budget info đầy đủ

---

## 🎯 OPTION 2: IMPORT VÀO EXCEL

### Cho ai?
- **Project managers cần edit/track**
- **Teams muốn customize view**
- **Leadership muốn filter/sort**

### Bước 1: Import CSV vào Excel

```bash
File → Open → ITSM-Roadmap-Gantt.csv
```

Hoặc:
```bash
Data → Get Data → From Text/CSV → ITSM-Roadmap-Gantt.csv
```

### Bước 2: Format Data

Excel sẽ auto-detect columns. Verify:
- `Start_Date` & `End_Date` format: YYYY-MM-DD
- `Duration_Days` format: Number
- `Budget_USD` format: Currency

### Bước 3: Create Gantt Chart trong Excel

#### Method A: Using Excel Add-in
1. Install "Office Timeline" hoặc "TeamGantt" add-in (free)
2. Select all data
3. Click "Insert Timeline" từ add-in menu
4. Customize view: Show/hide columns, color by priority

#### Method B: Manual Conditional Formatting
1. Insert columns for each week (Jan W1, Jan W2, etc.)
2. Use formula để check nếu task active trong week đó:
   ```excel
   =IF(AND(Start_Date<=WeekEnd, End_Date>=WeekStart), "█", "")
   ```
3. Conditional formatting: Color cells theo Priority
4. Freeze panes để giữ task names khi scroll

### Bước 4: Add Charts & Dashboards

**Budget Timeline Chart:**
```excel
- Pivot Table: Sum Budget_USD by Phase
- Chart Type: Stacked Column Chart
```

**Resource Loading Chart:**
```excel
- Pivot Table: Count tasks by Owner & Month
- Chart Type: Heatmap or Stacked Area
```

**Progress Tracking:**
```excel
- Add column "Status" với dropdown: Not Started, In Progress, Completed
- Formula: % Complete = COUNT(Completed) / COUNT(Total)
```

### Advantages:
✅ Editable, trackable
✅ Can add actual dates vs planned
✅ Filter & sort powerful
✅ Export to PDF easily

### Limitations:
⚠️ Manual Gantt bar formatting effort
⚠️ Không có auto-dependency arrows

---

## 🎯 OPTION 3: IMPORT VÀO MS PROJECT

### Cho ai?
- **Professional project managers**
- **Organizations có MS Project licenses**
- **Teams cần advanced features (critical path, resource leveling)**

### Bước 1: Import CSV

```bash
File → New → Blank Project
File → Open → ITSM-Roadmap-Gantt.csv
```

MS Project sẽ launch "Import Wizard":
1. **Select Map:** Choose "New map"
2. **Map Tasks:**
   - Task_ID → ID
   - Task_Name → Name
   - Start_Date → Start
   - End_Date → Finish
   - Duration_Days → Duration (convert to days)
   - Dependencies → Predecessors
   - Owner → Resource Names
   - Priority → Priority
3. Click "Finish"

### Bước 2: Setup Dependencies

MS Project format cho dependencies: `Task_ID` (e.g., "1.1", "2.2")

If dependencies không import đúng, manually add:
```
Right-click task → Task Information → Predecessors tab → Add
```

### Bước 3: Assign Resources

1. Go to **Resource Sheet** view
2. Add all resources (owners):
   - CMDB Admin, 3rd Party Lead, CM Lead, IM Manager, etc.
3. Assign to tasks: Double-click task → Resources tab

### Bước 4: Setup Calendar

1. **Project → Project Information**
2. Set Start Date: 2026-01-06
3. Set Calendar: Standard (Mon-Fri work week)

### Bước 5: Customize Views

**Gantt Chart View:**
- Format → Bar Styles → Color by Priority
- Show critical path: Format → Critical Tasks (red color)

**Resource Usage View:**
- View → Resource Usage
- See workload per resource per week
- Identify overallocations (red color)

**Timeline View:**
- View → Timeline
- Add milestones (Q1/Q2/Q3/Q4 checkpoints)
- Export timeline for presentations

### Advantages:
✅ Professional Gantt với dependencies auto
✅ Critical path calculation automatic
✅ Resource leveling & conflict detection
✅ Baseline vs actual tracking
✅ Export high-quality timelines for reports

### Limitations:
⚠️ Requires MS Project license ($$$)
⚠️ Steeper learning curve

---

## 🎯 OPTION 4: IMPORT VÀO ONLINE TOOLS

### Recommended Free/Freemium Tools:

#### **1. TeamGantt** (https://teamgantt.com)
- **Best for:** Teams collaboration, simple UI
- **Import:** CSV upload → Map columns
- **Features:** Drag-drop editing, team sharing, progress tracking
- **Pricing:** Free for 1 project, $19/user/month for more

#### **2. GanttProject** (https://ganttproject.biz)
- **Best for:** Free, open-source, local install
- **Import:** File → Import → CSV
- **Features:** Full Gantt, resource leveling, export PDF
- **Pricing:** 100% FREE

#### **3. Monday.com Gantt View**
- **Best for:** Teams already on Monday.com
- **Import:** Import CSV as board → Switch to Gantt view
- **Features:** Automation, integrations, beautiful UI
- **Pricing:** $8/user/month

#### **4. Smartsheet Gantt**
- **Best for:** Enterprise, Excel-like interface
- **Import:** Import CSV → Convert to Gantt
- **Features:** Powerful formulas, dashboards, reports
- **Pricing:** $7/user/month

#### **5. Asana Timeline View**
- **Best for:** Task management + Gantt
- **Import:** CSV import → Timeline view
- **Features:** Task dependencies, team collaboration
- **Pricing:** Free for basic, $10.99/user/month for Timeline

### Import Steps (Generic):

1. **Upload CSV:**
   ```
   Import/Upload → Select ITSM-Roadmap-Gantt.csv
   ```

2. **Map Columns:**
   ```
   Task Name → Task_Name
   Start Date → Start_Date
   End Date → End_Date
   Assignee → Owner
   Dependencies → Dependencies column
   ```

3. **Customize:**
   - Color code by Priority
   - Group by Phase (Q1, Q2, Q3, Q4)
   - Add milestones for checkpoints

4. **Share:**
   - Generate share link for stakeholders
   - Export PDF/PNG for presentations
   - Embed in Confluence/Notion if supported

---

## 🎯 OPTION 5: CUSTOM VISUALIZATION VỚI PYTHON

### Cho ai?
- **Data analysts/engineers**
- **Teams muốn fully customized charts**
- **Automation & integration needs**

### Python Libraries:

**1. Plotly (Interactive Gantt)**
```python
import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv('ITSM-Roadmap-Gantt.csv')

# Convert dates
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Create Gantt
fig = px.timeline(
    df,
    x_start='Start_Date',
    x_end='End_Date',
    y='Task_Name',
    color='Priority',
    hover_data=['Owner', 'OC_Mapping', 'Budget_USD']
)

fig.update_yaxes(autorange="reversed")
fig.show()
```

**2. Matplotlib + mpltern (Static Gantt)**
```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('ITSM-Roadmap-Gantt.csv')
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

fig, ax = plt.subplots(figsize=(20, 10))

for idx, row in df.iterrows():
    ax.barh(
        row['Task_Name'],
        (row['End_Date'] - row['Start_Date']).days,
        left=row['Start_Date'],
        color='blue' if row['Priority']=='CRITICAL' else 'gray'
    )

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.tight_layout()
plt.savefig('gantt_chart.png', dpi=300)
```

---

## 📊 RECOMMENDED APPROACH BY USE CASE

| Use Case | Recommended Tool | Reason |
|----------|------------------|--------|
| **Quick view for leadership** | Markdown file | No setup, visual, comprehensive |
| **Project tracking & updates** | Excel + Office Timeline | Familiar, editable, exportable |
| **Professional PM** | MS Project | Full features, critical path, resource mgmt |
| **Team collaboration** | TeamGantt or Monday.com | Real-time updates, sharing easy |
| **Free & powerful** | GanttProject (desktop) | Open-source, full-featured |
| **Integration with Jira** | Jira Timeline view | Import CSV as tasks, native integration |
| **Custom dashboards** | Python Plotly | Fully customizable, automation |
| **Presentation to execs** | PowerPoint with timeline screenshot | Clean, simplified, no details overload |

---

## 🔄 UPDATING THE GANTT CHART

### When to Update?

**Weekly (Recommended):**
- Mark tasks "In Progress" or "Completed"
- Update actual start/end dates if different from plan

**Monthly (Must):**
- Update after Q review meetings
- Adjust future tasks based on delays/speedups
- Update budget actual vs planned

### How to Update?

**Option A: Direct CSV Edit**
1. Open CSV in Excel or text editor
2. Update Status column: "Not Started" → "In Progress" → "Completed"
3. Add actual dates in new columns: "Actual_Start", "Actual_End"
4. Re-import to tool of choice

**Option B: Update in Tool**
1. If using MS Project, TeamGantt, etc., update directly in tool
2. Export back to CSV: File → Export → CSV
3. Replace old CSV file

**Option C: Versioning**
```bash
ITSM-Roadmap-Gantt-2026-01-06-v1.csv
ITSM-Roadmap-Gantt-2026-02-01-v2.csv
ITSM-Roadmap-Gantt-2026-03-01-v3.csv
```

---

## 📈 CREATING DASHBOARDS & REPORTS

### Dashboard 1: Executive Timeline (PowerPoint/Google Slides)

**What to show:**
- Q1-Q4 phases with major milestones
- Current progress % (from Status column)
- Critical path highlighted
- Budget cumulative spend

**How:**
1. Take screenshot of Gantt chart (from tool or markdown)
2. Annotate with highlights/arrows
3. Add progress bars for OC1-OC4
4. Add status: On Track / At Risk / Delayed

### Dashboard 2: Resource Heatmap (Excel)

**What to show:**
- Each resource (owner) as row
- Each month as column
- Color intensity = number of tasks

**How:**
1. Pivot Table: Rows=Owner, Columns=Month, Values=Count of tasks
2. Conditional Formatting: Color scale (white to red)
3. Highlight overallocations (>3 tasks/month)

### Dashboard 3: Budget Tracking (Excel)

**What to show:**
- Planned budget cumulative by quarter
- Actual spend (update monthly)
- Variance

**How:**
1. Pivot Table: Sum Budget_USD by Phase
2. Line chart: Planned vs Actual cumulative
3. Add variance % formula

---

## 🚀 INTEGRATION WITH OTHER TOOLS

### Integration with Jira:

1. **Import as Epics/Tasks:**
   - Use Jira CSV importer
   - Map Task_ID → Issue Key, Task_Name → Summary
   - Map Phase → Epic, Owner → Assignee

2. **Link to existing Jira projects:**
   - Add "Jira_Key" column to CSV
   - Reference existing tickets: "ITSM-123", "QA-456"

3. **Sync with Jira Timeline:**
   - Jira → Timeline view shows imported tasks
   - Update in Jira, export CSV for reporting

### Integration with Confluence:

1. **Embed Gantt visualization:**
   - Upload PNG/PDF of Gantt to Confluence page
   - Update monthly with new versions

2. **Link CSV as attachment:**
   - Attach CSV file to Confluence page
   - Stakeholders can download for their own use

### Integration with Google Sheets:

1. **Import CSV:**
   ```
   File → Import → Upload → ITSM-Roadmap-Gantt.csv
   ```

2. **Use Google Sheets Gantt Add-ons:**
   - "ProjectSheet Planning" (free)
   - "Gantter" (freemium)

3. **Share with stakeholders:**
   - Share → Anyone with link can view
   - Real-time collaboration for updates

---

## ❓ FAQ & TROUBLESHOOTING

### Q: Dates không hiển thị đúng khi import vào Excel?
**A:** Excel có thể interpret dates sai. Fix:
1. Select date columns
2. Format Cells → Date → YYYY-MM-DD
3. Hoặc dùng formula: `=DATEVALUE(A2)` để convert text to date

### Q: Dependencies không work trong MS Project?
**A:** MS Project cần format "Task_ID" (e.g., "1.1FS", "2.2SS").
- FS = Finish-to-Start (default)
- SS = Start-to-Start
- FF = Finish-to-Finish
Check Dependencies column format.

### Q: Tool tôi dùng không support CSV import?
**A:** Copy-paste alternative:
1. Open CSV in Excel
2. Select all data
3. Copy → Paste into tool (Google Sheets, Monday.com, etc.)
4. Map columns manually if needed

### Q: Làm sao track actual vs planned?
**A:** Add 2 columns mới vào CSV:
- `Actual_Start_Date`
- `Actual_End_Date`
Update monthly. Most tools support baseline comparison.

### Q: Gantt chart quá dài, không fit 1 trang?
**A:** Options:
1. Filter by Phase: Show chỉ Q1, sau đó Q2, etc.
2. Group by Phase: Collapse details, show high-level only
3. Use "zoom out" feature in tools
4. Split into multiple charts: "Q1-Q2" and "Q3-Q4"

---

## 📞 SUPPORT & UPDATES

### Need Help?
- Check tool's documentation (Excel, MS Project, TeamGantt, etc.)
- ITSM team lead có thể assist với roadmap questions
- Jira Admin có thể help với Jira integration

### Roadmap Updates:
- CSV file sẽ được update monthly (after each Q review)
- Version naming: `ITSM-Roadmap-Gantt-YYYY-MM-DD-vX.csv`
- Check `/reports` directory cho latest version

### Feedback:
Nếu có suggestions để improve Gantt chart format or tooling, please provide feedback to ITSM Lead.

---

**Last Updated:** 2025-12-02
**Version:** 1.0
**Maintainer:** ITSM Team

