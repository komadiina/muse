import WelcomeHeader from "@/components/WelcomeHeader";

export default function Home() {
  return (
    <div className={"max-w-screen-2xl mx-auto h-screen min-h-screen"}>
      <div className={"flex flex-col items-start justify-start top-1/2 absolute"}>
        <WelcomeHeader/>
      </div>
    </div>
  );
}
