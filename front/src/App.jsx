import React, { useState, useRef } from 'react';
import './App.css';
import { FaMicrophone, FaPaperclip, FaRobot, FaBell, FaCog } from 'react-icons/fa';

const AGENT_MODES = [
  { name: 'Gemini', icon: <FaRobot /> },
  { name: 'ChatGPT', icon: <FaRobot /> },
  { name: 'Custom', icon: <FaRobot /> },
];

function App() {
  const [messages, setMessages] = useState([
    { sender: 'agent', text: '👋 Hi! I am Aura, your accessibility-first AI assistant. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [mode, setMode] = useState(AGENT_MODES[0].name);
  const [showSettings, setShowSettings] = useState(false);
  const [showNotifications, setShowNotifications] = useState(false);
  const fileInputRef = useRef();

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: 'user', text: input }]);
    setInput('');
    // TODO: Call backend API with input and mode
    setTimeout(() => {
      setMessages(msgs => [...msgs, { sender: 'agent', text: `(${mode} mode) [Stub] Response to: "${input}"` }]);
    }, 800);
  };

  const handleVoiceInput = () => {
    // TODO: Integrate Web Speech API or backend STT
    setInput(input + ' [🎤 Voice input stub]');
  };

  const handleFileUpload = e => {
    const file = e.target.files[0];
    if (file) {
      setMessages([...messages, { sender: 'user', text: `📎 Uploaded file: ${file.name}` }]);
      // TODO: Send file to backend
    }
  };

  return (
    <div className="aura-app">
      <header className="aura-header">
        <div className="aura-logo">🌈 Aura</div>
        <div className="aura-modes">
          {AGENT_MODES.map(m => (
            <button
              key={m.name}
              className={`aura-mode-btn${mode === m.name ? ' active' : ''}`}
              onClick={() => setMode(m.name)}
              aria-label={`Switch to ${m.name} mode`}
            >
              {m.icon} {m.name}
            </button>
          ))}
        </div>
        <div className="aura-actions">
          <button className="aura-icon-btn" onClick={() => setShowNotifications(!showNotifications)} aria-label="Notifications"><FaBell /></button>
          <button className="aura-icon-btn" onClick={() => setShowSettings(!showSettings)} aria-label="Settings"><FaCog /></button>
        </div>
      </header>
      <main className="aura-chat">
        <div className="aura-messages" aria-live="polite">
          {messages.map((msg, i) => (
            <div key={i} className={`aura-message ${msg.sender}`}> 
              <div className="aura-avatar">{msg.sender === 'agent' ? '🤖' : '🧑'}</div>
              <div className="aura-bubble">{msg.text}</div>
            </div>
          ))}
        </div>
        <div className="aura-input-row">
          <button className="aura-icon-btn" onClick={handleVoiceInput} aria-label="Voice input"><FaMicrophone /></button>
          <input
            className="aura-input"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSend()}
            placeholder="Type your message..."
            aria-label="Chat input"
          />
          <button className="aura-icon-btn" onClick={() => fileInputRef.current.click()} aria-label="Upload file"><FaPaperclip /></button>
          <input type="file" ref={fileInputRef} style={{ display: 'none' }} onChange={handleFileUpload} />
          <button className="aura-send-btn" onClick={handleSend} aria-label="Send">Send</button>
        </div>
      </main>
      {showNotifications && (
        <aside className="aura-notifications" tabIndex={0} aria-label="Notifications">
          <h2>Notifications</h2>
          <ul>
            <li>🔔 You have 1 urgent email from your doctor.</li>
            <li>📅 You have a meeting in 15 minutes.</li>
            <li>🔓 Your front door is unlocked.</li>
          </ul>
        </aside>
      )}
      {showSettings && (
        <aside className="aura-settings" tabIndex={0} aria-label="Settings">
          <h2>Settings</h2>
          <label>
            <span>Font size</span>
            <input type="range" min="14" max="28" defaultValue="18" />
          </label>
          <label>
            <span>Contrast</span>
            <select>
              <option>Normal</option>
              <option>High Contrast</option>
              <option>Dark</option>
            </select>
          </label>
          <label>
            <span>Agent Tone</span>
            <select>
              <option>Friendly</option>
              <option>Professional</option>
              <option>Playful</option>
            </select>
          </label>
        </aside>
      )}
    </div>
  );
}

export default App;
