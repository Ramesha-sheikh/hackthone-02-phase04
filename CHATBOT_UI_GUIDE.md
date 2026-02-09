# AI Chatbot UI Guide

## 🎨 Visual Layout

### Dashboard with Chatbot

```
┌─────────────────────────────────────────────────────────────┐
│  Dashboard                                    Welcome, User! │
│                                                    [Logout]  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  📝 Add New Todo                                             │
│  ┌───────────────────────────────────────────────────┐      │
│  │ Title: [________________________]                 │      │
│  │ Description: [_____________________]              │      │
│  │              [_____________________]              │      │
│  │              [_____________________]              │      │
│  │                                                    │      │
│  │                         [Add Todo]                │      │
│  └───────────────────────────────────────────────────┘      │
│                                                               │
│  📋 Your Todos                                               │
│  ┌───────────────────────────────────────────────────┐      │
│  │ ☐ Task 1                    [✓] [Edit] [Delete]  │      │
│  │ ☐ Task 2                    [✓] [Edit] [Delete]  │      │
│  │ ☑ Task 3 (completed)        [✓] [Edit] [Delete]  │      │
│  └───────────────────────────────────────────────────┘      │
│                                                               │
│                                                               │
│                                                        ┌────┐ │
│                                                        │ 💬 │ │ ← Chatbot Button
│                                                        └────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Chatbot Opened

```
┌─────────────────────────────────────────────────────────────┐
│  Dashboard                                                    │
│                                                               │
│  [Your tasks and content here...]                            │
│                                                               │
│                                              ┌──────────────┐ │
│                                              │ AI Assistant │ │
│                                              │ 🟢 Online [X]│ │
│                                              ├──────────────┤ │
│                                              │              │ │
│                                              │ 🤖 Hello!   │ │
│                                              │ How can I   │ │
│                                              │ help you?   │ │
│                                              │              │ │
│                                              │       You 👤│ │
│                                              │ Show my     │ │
│                                              │ tasks       │ │
│                                              │              │ │
│                                              │ 🤖 You have │ │
│                                              │ 3 tasks:    │ │
│                                              │ 1. Task 1   │ │
│                                              │ 2. Task 2   │ │
│                                              │ 3. Task 3   │ │
│                                              │              │ │
│                                              ├──────────────┤ │
│                                              │ Type here... │ │
│                                              │          [→] │ │
│                                              └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🎨 Color Scheme

### Chatbot Button
- **Closed**: Caramel gold gradient (#d9a441 to #8d6e63)
- **Open**: Coffee brown gradient (#8d6e63 to #5d4037)
- **Glow**: Animated glow effect matching theme
- **Size**: 64x64px circular button
- **Position**: Fixed bottom-right, 24px from edges

### Chatbot Window
- **Size**: 384px width × 512px height
- **Position**: Bottom-right, above the button
- **Background**: Coffee card color (var(--bg-card))
- **Border**: 2px solid coffee brown (#8d6e63)
- **Shadow**: Glowing shadow effect

### Messages
- **User Messages**:
  - Background: Caramel gradient (#d9a441 to #8d6e63)
  - Text: Dark coffee (#3c2f2f)
  - Alignment: Right

- **AI Messages**:
  - Background: Card background
  - Text: Primary text color
  - Border: Coffee brown
  - Alignment: Left

## 🎭 Animations

### Button Hover
```css
transform: scale(1.1)
box-shadow: 0 0 25px caramel-glow
transition: 300ms
```

### Button Click
```css
transform: scale(0.95)
transition: 150ms
```

### Message Appearance
```css
fade-in + slide-up animation
duration: 300ms
easing: ease-out
```

### Loading Dots
```css
3 dots bouncing animation
staggered delay: 0s, 0.2s, 0.4s
```

## 📱 Responsive Behavior

### Desktop (>768px)
- Full-size chatbot (384px × 512px)
- Fixed position bottom-right
- Button size: 64px

### Mobile (<768px)
- Full-screen chatbot overlay
- Button size: 56px
- Window covers entire viewport

## 🎯 Interactive States

### Button States
1. **Default**: Caramel glow, message icon
2. **Hover**: Scaled up (110%), brighter glow
3. **Active**: Scaled down (95%)
4. **Open**: Coffee brown, X icon
5. **Offline**: Reduced opacity (50%), no glow

### Window States
1. **Loading**: Animated dots
2. **Active**: Normal
3. **Error**: Red border accent
4. **Empty**: Welcome message shown

## 💡 User Experience Features

### 1. Welcome Message
```
🤖 Hello! I'm your AI task assistant.

You can ask me to:
• Add new tasks
• Show your tasks
• Update tasks
• Delete tasks

How can I help you today?
```

### 2. Real-time Feedback
- Typing indicators (3 bouncing dots)
- Message timestamps
- Delivery confirmation
- Error messages in red

### 3. Auto-scroll
- New messages auto-scroll into view
- Smooth scrolling animation
- Maintains scroll position when typing

### 4. Input Field
- Placeholder: "Ask me to add, list, update, or delete tasks..."
- Auto-focus on window open
- Enter to send
- Disabled when loading or offline

## 🎨 Theme Integration Examples

### Coffee Brown Buttons
```css
background: linear-gradient(135deg, #5d4037, #8d6e63)
color: #f5f1ee (cream)
box-shadow: 0 0 15px rgba(93, 64, 55, 0.4)
```

### Caramel Accents
```css
border-color: #d9a441
box-shadow: 0 0 20px rgba(217, 164, 65, 0.6)
```

### Card Style
```css
background: var(--bg-card)
border: 1px solid var(--border-coffee)
box-shadow: 0 2px 10px rgba(141, 110, 99, 0.2)
```

## 📐 Measurements

```
Chatbot Button:
├─ Width: 64px
├─ Height: 64px
├─ Border-radius: 50% (circle)
├─ Bottom: 24px
└─ Right: 24px

Chatbot Window:
├─ Width: 384px
├─ Height: 512px
├─ Border-radius: 12px
├─ Bottom: 96px (button height + spacing)
└─ Right: 24px

Header:
├─ Height: 60px
├─ Padding: 16px
└─ Background: Gradient

Messages Area:
├─ Flex-grow: 1
├─ Padding: 16px
├─ Overflow-y: auto
└─ Background: Primary

Input Area:
├─ Height: 80px
├─ Padding: 16px
└─ Border-top: 1px solid
```

## 🔄 State Flow

```
User clicks button
        ↓
Window opens with fade-in
        ↓
Welcome message displays
        ↓
User types message
        ↓
Input field active
        ↓
User sends (Enter or Button)
        ↓
Message appears on right
        ↓
Loading dots appear
        ↓
AI response arrives
        ↓
Response displays on left
        ↓
Dashboard refreshes (if task operation)
```

## ✅ Accessibility Features

- **Keyboard Navigation**: Tab to focus, Enter to send
- **Screen Reader**: Proper ARIA labels
- **Color Contrast**: WCAG AA compliant
- **Focus Indicators**: Visible focus states
- **Error Messages**: Clear and descriptive

## 🎬 Animation Timing

```css
Button hover: 300ms ease-out
Button click: 150ms ease-in
Window open/close: 300ms ease-out
Message appear: 300ms ease-out
Loading dots: 1.4s infinite
Scroll animation: 500ms ease-in-out
```

---

**Design System**: Coffee & Caramel Theme
**Component**: AI Chatbot Widget
**Status**: Production Ready ✅
