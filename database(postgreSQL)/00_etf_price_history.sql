CREATE TABLE etf_price_history (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    etf_id INTEGER NOT NULL,

    price_date DATE NOT NULL,

    close_price NUMERIC(10,2),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_price_etf
        FOREIGN KEY(etf_id)
        REFERENCES etf_info(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_price
        UNIQUE(etf_id, price_date)
);