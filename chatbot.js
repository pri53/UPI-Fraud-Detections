import React, { useState } from 'react';
import './chatbot.css';

const Chatbot = ({ onClose }) => {
    const [messages, setMessages] = useState([
        { text: "Hello! I'm your UPI assistant. How can I help you with UPI transactions today?", sender: 'bot' }
    ]);
    const [inputMessage, setInputMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSendMessage = async () => {
        if (!inputMessage.trim()) return;

        const userMessage = { text: inputMessage, sender: 'user' };
        setMessages(prev => [...prev, userMessage]);
        setInputMessage('');
        setIsLoading(true);

        try {
            const response = await fetch('http://localhost:5051/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: inputMessage }),
            });

            const data = await response.json();
            if (data.status === 'success') {
                setMessages(prev => [...prev, { text: data.response, sender: 'bot' }]);
            } else {
                setMessages(prev => [...prev, { text: "Sorry, I couldn't process your request.", sender: 'bot' }]);
            }
        } catch (error) {
            setMessages(prev => [...prev, { text: "Error connecting to the chat service.", sender: 'bot' }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="chatbot-container">
            <div className="chatbot-header">
                <h3>UPI Assistant</h3>
                <button onClick={onClose} className="close-btn">×</button>
            </div>
            <div className="chatbot-messages">
                {messages.map((message, index) => (
                    <div key={index} className={`message ${message.sender}`}>
                        {message.text}
                    </div>
                ))}
                {isLoading && <div className="message bot">Typing...</div>}
            </div>
            <div className="chatbot-input">
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    placeholder="Ask about UPI..."
                    onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                />
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chatbot;