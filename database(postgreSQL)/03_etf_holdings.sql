CREATE TABLE etf_holdings (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    snapshot_id INTEGER NOT NULL,

    rank SMALLINT NOT NULL,
    stock_symbol VARCHAR(10) NOT NULL,
    stock_name VARCHAR(100) NOT NULL,
    weight NUMERIC(6,2) NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_holding_snapshot
        FOREIGN KEY (snapshot_id)
        REFERENCES etf_snapshot(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_holding_rank
        UNIQUE(snapshot_id, rank)
);