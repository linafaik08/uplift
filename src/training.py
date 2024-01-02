from causalml.inference.tree import UpliftTreeClassifier, UpliftRandomForestClassifier
import pandas as pd
import numpy as np
import itertools


def evaluate(
        df, cols_features, col_target,
        uplift_model, score_function, score_args={}):
    if "UpliftRandomForestClassifier" in str(uplift_model.__class__):
        pred_df = uplift_model.predict(df[cols_features].values, full_output=True)[uplift_model.classes_]
    else:
        pred_df = pd.DataFrame(
            uplift_model.predict(df[cols_features].values),
            columns=uplift_model.classes_)

    pred_df["best_treatment_index"] = np.argmax(pred_df.values, axis=1)
    pred_df["best_treatment"] = pred_df["best_treatment_index"].map(
        {i: c for i, c in enumerate(uplift_model.classes_)}
    )
    pred_df["uplift"] = pred_df.apply(lambda df: df[df["best_treatment"]], axis=1)

    score = score_function(
        y_true=df[col_target],
        uplift=pred_df["uplift"],
        treatment=df["treatment_group"].replace({"treatment": 1, "control": 0}),
        **score_args
    )

    return score