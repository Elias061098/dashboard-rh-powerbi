-- Schéma PostgreSQL — Dashboard RH

CREATE TABLE employes (
    employe_id      SERIAL PRIMARY KEY,
    departement     VARCHAR(50),
    niveau          VARCHAR(20),
    anciennete_ans  DECIMAL(4,1),
    salaire         INTEGER,
    score_performance DECIMAL(3,1),
    jours_absence   INTEGER,
    a_quitte        SMALLINT DEFAULT 0
);

-- Vue turnover par département
CREATE VIEW v_turnover_dept AS
SELECT
    departement,
    COUNT(*)                                      AS nb_employes,
    SUM(a_quitte)                                 AS nb_departs,
    ROUND(AVG(a_quitte) * 100, 1)                 AS taux_turnover_pct,
    ROUND(AVG(jours_absence), 1)                  AS abs_moyenne,
    ROUND(AVG(score_performance), 1)              AS perf_moyenne
FROM employes
GROUP BY departement
ORDER BY taux_turnover_pct DESC;

-- Vue corrélation performance / départ
CREATE VIEW v_perf_turnover AS
SELECT
    CASE
        WHEN score_performance < 3  THEN '< 3'
        WHEN score_performance < 5  THEN '3-5'
        WHEN score_performance < 7  THEN '5-7'
        ELSE '> 7'
    END AS tranche_perf,
    COUNT(*)                              AS nb_employes,
    ROUND(AVG(a_quitte) * 100, 1)         AS taux_turnover_pct
FROM employes
GROUP BY tranche_perf
ORDER BY taux_turnover_pct DESC;
