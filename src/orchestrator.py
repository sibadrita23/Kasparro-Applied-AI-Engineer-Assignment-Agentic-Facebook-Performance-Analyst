import yaml, json
from src.agents.planner_agent import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent
from src.utils.logger import log_run

class Orchestrator:
    def __init__(self):
        with open('config/config.yaml') as f:
            self.config = yaml.safe_load(f)
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative_agent = CreativeAgent()

    def run(self, query):
        subtasks = self.planner.plan(query)
        stats, df = self.data_agent.load_and_summarize(self.config['paths']['data'])
        hypos = self.insight_agent.generate(stats, df)
        validated = self.evaluator.evaluate(hypos, stats, df)
        with open(self.config['paths']['insights'], 'w') as f:
            json.dump(validated, f, indent=2)
        creatives = self.creative_agent.recommend(df, self.config['thresholds']['ctr_low'])
        with open(self.config['paths']['creatives'], 'w') as f:
            json.dump(creatives, f, indent=2)
        log_run(self.config['paths']['logs'], validated, creatives)
        self._write_report(validated, creatives)

    def _write_report(self, insights, creatives):
        with open(self.config['paths']['report'], 'w') as f:
            f.write("# Facebook Ads Performance Report\n\n")
            f.write("## Insights\n")
            for i in insights:
                f.write(f"- Reason: {i['reason']}\n  Summary: {i['summary']}\n  Confidence: {i['confidence']:.2f}\n  Evidence: {i['evidence']}\n\n")
            f.write("## Creative Recommendations\n")
            for c in creatives:
                f.write(f"- Campaign: {c['campaign_name']}\n  Headline: {c['headline']}\n  Message: {c['message']}\n  CTA: {c['cta']}\n\n")
