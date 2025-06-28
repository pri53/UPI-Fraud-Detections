
// import React, { useState } from "react";
// import axios from "axios";
// import './TransactionForm.css';



// function TransactionForm() {
//   const [formData, setFormData] = useState({
//     amount: "",
//     time: "",
//     from: "",
//     to: "",
//     transaction_id: "",
//   });

//   const [result, setResult] = useState(null);

//   const handleChange = (e) => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post("http://localhost:5050/predict", formData);
//       setResult(response.data);
//     } catch (error) {
//       console.error("Error:", error);
//       setResult({ status: "error", confidence: 0 });
//     }
//   };

//   return (
//     <div>
//       <form onSubmit={handleSubmit} style={{ display: "grid", gap: "10px", maxWidth: 400 }}>
//         <input name="amount" placeholder="Amount" value={formData.amount} onChange={handleChange} required />
//         <input name="time" placeholder="Time (HH:MM)" value={formData.time} onChange={handleChange} required />
//         <input name="from" placeholder="From" value={formData.from} onChange={handleChange} required />
//         <input name="to" placeholder="To" value={formData.to} onChange={handleChange} required />
//         <input name="transaction_id" placeholder="Transaction ID" value={formData.transaction_id} onChange={handleChange} required />
//         <button type="submit">Check Transaction</button>
//       </form>
//       {result && (
//         <div style={{ marginTop: 20 }}>
//           <h3>Prediction: {result.status}</h3>
//           <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default TransactionForm;



import React, { useState } from 'react';
import './TransactionForm.css';
import Chatbot from './chatbot';


const TransactionForm = () => {
    const [formData, setFormData] = useState({
        transaction_id: '',
        from: '',
        to: '',
        amount: '',
        time: '',
        location: '', // new field
        area: '',      // new field
    });
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [showChatbot, setShowChatbot] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch('http://localhost:5051/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const data = await response.json();
            
            if (data.status === 'success') {
                setResult(data);
            } else {
                setError(data.message || 'Prediction failed');
            }
        } catch (err) {
            setError('Failed to connect to the server');
        } finally {
            setLoading(false);
        }
    };

//     return (
//         <div className="container">
//             <h2>UPI Fraud Detection</h2>
//             <form onSubmit={handleSubmit}>
//                 <input
//                     type="text"
//                     name="transaction_id"
//                     placeholder="Transaction ID"
//                     value={formData.transaction_id}
//                     onChange={handleChange}
//                     required
//                 />
//                 <input 
//                     name="location" 
//                     placeholder="City" 
//                     value={formData.location} 
//                     onChange={handleChange} 
//                     required
//                 />
//                 <input 
//                     name="area" 
//                     placeholder="Area" 
//                     value={formData.area} 
//                     onChange={handleChange} 
//                     required
//                 />

//                 <input
//                     type="text"
//                     name="from"
//                     placeholder="From (e.g., user@bank)"
//                     value={formData.from}
//                     onChange={handleChange}
//                     required
//                 />
//                 <input
//                     type="text"
//                     name="to"
//                     placeholder="To (e.g., merchant@upi)"
//                     value={formData.to}
//                     onChange={handleChange}
//                     required
//                 />
//                 <input
//                     type="number"
//                     name="amount"
//                     placeholder="Amount"
//                     value={formData.amount}
//                     onChange={handleChange}
//                     required
//                 />
//                 <input
//                     type="text"
//                     name="time"
//                     placeholder="Time (HH:MM)"
//                     value={formData.time}
//                     onChange={handleChange}
//                     required
//                 />
//                 <button type="submit" disabled={loading}>
//                     {loading ? 'Processing...' : 'Check Transaction'}
//                 </button>
//             </form>

//             {error && <div className="error-message">{error}</div>}

//             {result && (
//                 <div className={`result-box ${result.prediction}`}>
//                     <h3>Result: {result.prediction === 'fraud' ? 'Fraud Detected!' : 'Legitimate Transaction'}</h3>

//                     <p>Confidence: {result.confidence}%</p>
//                     {result.prediction === "legitimate" && (
//                     <p style={{ color: "green" }}>✅ This transaction appears to be legitimate.</p>
//                      )}
//                     {result.prediction === 'fraud' && (
//                         <p className="warning">⚠️ Warning: This transaction appears suspicious!</p>
                        
//                     )}
//                     <h4>What to do:</h4>
//                             <ul>
//                                 {result.action_required.steps_to_follow.map((step, index) => (
//                                     <li key={index}>{step}</li>
//                                 ))}
//                             </ul>
//                             <h4>Helpful Links:</h4>
//                             <ul>
//                                 <li><a href={result.action_required.complaint_links.national_cyber_crime_portal} target="_blank" rel="noopener noreferrer">Cyber Crime Portal</a></li>
//                                 <li><a href={result.action_required.complaint_links.rbi_banking_ombudsman} target="_blank" rel="noopener noreferrer">RBI Ombudsman</a></li>
//                                 <li><a href={result.action_required.complaint_links.upi_dispute_resolution} target="_blank" rel="noopener noreferrer">UPI Dispute Resolution</a></li>
//                             </ul>
                    
//                 </div>
//             )}
            

//             <div 
//                 className="chatbot-toggle"
//                 onClick={() => setShowChatbot(!showChatbot)}
//             >
//                 💬
//             </div>

//             {showChatbot && <Chatbot onClose={() => setShowChatbot(false)} />}
//         </div>
//     );
// };

// export default TransactionForm;

return (
    <div className="container">
        <h2>UPI Fraud Detection</h2>
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="transaction_id"
                placeholder="Transaction ID"
                value={formData.transaction_id}
                onChange={handleChange}
                required
            />
            <input 
                name="location" 
                placeholder="City" 
                value={formData.location} 
                onChange={handleChange} 
                required
            />
            <input 
                name="area" 
                placeholder="Area" 
                value={formData.area} 
                onChange={handleChange} 
                required
            />
            <input
                type="text"
                name="from"
                placeholder="From (e.g., user@bank)"
                value={formData.from}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="to"
                placeholder="To (e.g., merchant@upi)"
                value={formData.to}
                onChange={handleChange}
                required
            />
            <input
                type="number"
                name="amount"
                placeholder="Amount"
                value={formData.amount}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="time"
                placeholder="Time (HH:MM)"
                value={formData.time}
                onChange={handleChange}
                required
            />
            <button type="submit" disabled={loading}>
                {loading ? 'Processing...' : 'Check Transaction'}
            </button>
        </form>

        {error && <div className="error-message">{error}</div>}

        {result && (
            <div className={`result-box ${result.prediction}`}>
                <h3>
                    Result: {result.prediction === 'fraud' ? 'Fraud Detected!' : 'Legitimate Transaction'}
                </h3>
                <p>Confidence: {result.confidence}%</p>

                {result.prediction === "legitimate" && (
                    <p style={{ color: "green" }}>✅ This transaction appears to be legitimate.</p>
                )}

                {result.prediction === 'fraud' && (
                    <>
                        <p className="warning">⚠️ Warning: This transaction appears suspicious!</p>

                        {result.action_required && result.action_required.steps_to_follow && (
                            <>
                                <h4>What to do:</h4>
                                <ul>
                                    {result.action_required.steps_to_follow.map((step, index) => (
                                        <li key={index}>{step}</li>
                                    ))}
                                </ul>
                            </>
                        )}

                        {result.action_required && result.action_required.complaint_links && (
                            <>
                                <h4>Helpful Links:</h4>
                                <ul>
                                    <li>
                                        <a
                                            href={result.action_required.complaint_links.national_cyber_crime_portal}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                        >
                                            Cyber Crime Portal
                                        </a>
                                    </li>
                                    <li>
                                        <a
                                            href={result.action_required.complaint_links.rbi_banking_ombudsman}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                        >
                                            RBI Ombudsman
                                        </a>
                                    </li>
                                    <li>
                                        <a
                                            href={result.action_required.complaint_links.upi_dispute_resolution}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                        >
                                            UPI Dispute Resolution
                                        </a>
                                    </li>
                                </ul>
                            </>
                        )}
                    </>
                )}
            </div>
        )}

        <div 
            className="chatbot-toggle"
            onClick={() => setShowChatbot(!showChatbot)}
        >
            💬
        </div>

        {showChatbot && <Chatbot onClose={() => setShowChatbot(false)} />}
    </div>
  );
  };

  export default TransactionForm;
