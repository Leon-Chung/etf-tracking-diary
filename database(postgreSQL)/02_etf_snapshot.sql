CREATE TABLE etf_snapshot (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    etf_id INTEGER NOT NULL,
    snapshot_date DATE NOT NULL,

    fund_size NUMERIC(18,2),
    beneficiaries INTEGER,
    management_fee NUMERIC(5,2),
	nav NUMERIC(10,2),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_snapshot_etf
        FOREIGN KEY (etf_id)
        REFERENCES etf_info(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_snapshot
        UNIQUE(etf_id, snapshot_date)
);