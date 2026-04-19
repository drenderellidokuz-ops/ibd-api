class Engine:

    def evaluate(self, data):

        flags = []
        explanations = []

        if data["labs"]["calprotectin"] > 250:
            flags.append("orta")
            explanations.append("Kalprotektin yüksek → inflamasyon")

        if data["labs"]["crp"] > 50:
            flags.append("ağır")
            explanations.append("CRP çok yüksek")

        if data["symptoms"]["blood_in_stool"]:
            flags.append("orta")
            explanations.append("Dışkıda kan var")

        severity = "hafif"

        if "ağır" in flags:
            severity = "ağır"
        elif "orta" in flags:
            severity = "orta"

        return {
            "severity": severity,
            "flags": list(set(flags)),
            "recommendation": "tedavi artırımı" if severity != "hafif" else "takip",
            "explanations": explanations
        }