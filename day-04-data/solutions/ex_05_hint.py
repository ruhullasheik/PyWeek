"""Hints for ex_05

    def flatten_dict(d, parent_key="", sep="."):
        result = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
            if isinstance(v, dict):
                result.update(flatten_dict(v, new_key, sep=sep))
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    result[f"{new_key}.{i}"] = item
            else:
                result[new_key] = v
        return result
"""
