CREATE TABLE IF NOT EXISTS models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('classification', 'regression')),
    hyperparameters JSONB NOT NULL,
    train_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS preprocessing (
    id SERIAL PRIMARY KEY,
    sampling_strategy VARCHAR(20) NOT NULL CHECK (sampling_strategy IN ('oversampling', 'none')),
    split_method VARCHAR(20) NOT NULL CHECK (split_method IN ('holdout', 'kfold', 'stratified')),
    normalized BOOLEAN NOT NULL,
    test_size FLOAT NOT NULL,
    test_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    model_id INT REFERENCES models(id),
    preprocessing_id INT REFERENCES preprocessing(id),
    test_size INT NOT NULL,
    dataset VARCHAR(50) NOT NULL,
    train_size INT NOT NULL,
    test_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS metrics (
    id SERIAL PRIMARY KEY,
    result_id INTEGER REFERENCES results(id),
    metric_name VARCHAR(20) NOT NULL CHECK (metric_name IN ('accuracy', 'precision', 'recall', 'f1', 'roc_auc', 'mse', 'mape', 'mae', 'r2')),
    metric_value FLOAT NOT NULL,
    test_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);