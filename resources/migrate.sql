CREATE DATABASE IF NOT EXISTS llm_messages
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE llm_messages;
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_type VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS analysis_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    source_code TEXT,
    sonar_output TEXT,
    codescene_output TEXT,
    llm_feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;