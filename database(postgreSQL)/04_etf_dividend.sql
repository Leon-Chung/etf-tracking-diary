CREATE TABLE etf_dividend (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    etf_id INTEGER NOT NULL,

    ex_dividend_date DATE NOT NULL,
    payment_date DATE,
    cash_dividend NUMERIC(10,2) NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_dividend_etf
        FOREIGN KEY (etf_id)
        REFERENCES etf_info(id)
        ON DELETE CASCADE
);